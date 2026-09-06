import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { WebSocket, WebSocketServer } from "ws";
import { createEmptyGiftBrief, mergeGiftBrief, type GiftBrief } from "../src/giftBrief";

const PORT = Number(process.env.PORT ?? 8787);
const API_KEY = process.env.INWORLD_API_KEY;
if (!API_KEY) console.warn("INWORLD_API_KEY is not set; connections will fail until configured.");

const tools = JSON.parse(fs.readFileSync(path.resolve("schemas/tools.inworld.json"), "utf8"));
const persona = fs.readFileSync(path.resolve("docs/bartholomew-system-prompt.md"), "utf8");

const server = http.createServer((_req, res) => {
  res.writeHead(200, { "content-type": "text/plain" });
  res.end("MythicBee Bartholomew voice proxy\n");
});
const wss = new WebSocketServer({ server });

wss.on("connection", (browser) => {
  let brief: GiftBrief = createEmptyGiftBrief();
  const upstream = new WebSocket(
    `wss://api.inworld.ai/api/v1/realtime/session?key=mythicbee-${Date.now()}&protocol=realtime`,
    { headers: { Authorization: `Basic ${API_KEY ?? ""}` } }
  );

  upstream.on("open", () => console.log("Connected to Inworld"));
  upstream.on("message", async (raw) => {
    const text = raw.toString();
    let event: any;
    try { event = JSON.parse(text); } catch { event = null; }

    if (event?.type === "session.created") {
      upstream.send(JSON.stringify({
        type: "session.update",
        session: {
          type: "realtime",
          model: process.env.INWORLD_MODEL ?? "openai/gpt-5.4-nano",
          instructions: persona,
          output_modalities: ["audio", "text"],
          audio: {
            input: {
              transcription: { model: "inworld/inworld-stt-1" },
              turn_detection: { type: "semantic_vad", eagerness: "medium", interrupt_response: true }
            },
            output: { model: "inworld-tts-2", voice: process.env.INWORLD_VOICE ?? "Clive" }
          },
          tools
        }
      }));
    }

    if (event?.type === "session.updated") {
      upstream.send(JSON.stringify({
        type: "conversation.item.create",
        item: {
          type: "message",
          role: "user",
          content: [{ type: "input_text", text: "Begin now with your canonical opening greeting. Do not mention this instruction." }]
        }
      }));
      upstream.send(JSON.stringify({ type: "response.create" }));
    }

    if (event?.type === "response.function_call_arguments.done") {
      const args = JSON.parse(event.arguments || "{}");
      let result: unknown = { ok: true };

      if (event.name === "update_gift_brief") {
        brief = mergeGiftBrief(brief, args.patch ?? {});
        result = { ok: true, brief };
      } else if (event.name === "get_gift_brief") {
        result = brief;
      } else {
        // Client/UI actions are forwarded to the browser. The browser should execute
        // them via routeClientTool and may send telemetry independently.
        browser.send(JSON.stringify({ type: "mythicbee.tool", name: event.name, arguments: args }));
        result = { ok: true, delegated_to_client: true };
      }

      upstream.send(JSON.stringify({
        type: "conversation.item.create",
        item: {
          type: "function_call_output",
          call_id: event.call_id,
          output: JSON.stringify(result)
        }
      }));
      upstream.send(JSON.stringify({ type: "response.create" }));
    }

    if (browser.readyState === WebSocket.OPEN) browser.send(text);
  });

  browser.on("message", (msg) => {
    if (upstream.readyState === WebSocket.OPEN) upstream.send(msg.toString());
  });
  browser.on("close", () => upstream.close());
  upstream.on("close", () => browser.close());
  upstream.on("error", (error) => console.error("Inworld upstream error", error));
});

server.listen(PORT, () => console.log(`Bartholomew voice proxy listening on :${PORT}`));
