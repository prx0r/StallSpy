import type { BartholomewController } from "./BartholomewController";

export interface InworldVoiceClientOptions {
  url?: string;
  controller: BartholomewController;
  onTool?: (name: string, args: any) => void | Promise<void>;
  onTranscript?: (role: "user" | "assistant", text: string) => void;
}

/**
 * Minimal browser-side WebSocket voice client for the included Inworld proxy.
 * It streams PCM16/24k mic audio and plays PCM16/24k output audio.
 * Production recommendation: replace ScriptProcessorNode with AudioWorklet.
 */
export class InworldVoiceClient {
  private ws: WebSocket | null = null;
  private audio: AudioContext | null = null;
  private mic: MediaStream | null = null;
  private processor: ScriptProcessorNode | null = null;
  private source: MediaStreamAudioSourceNode | null = null;
  private nextPlaybackTime = 0;
  private controller: BartholomewController;
  private onTool?: InworldVoiceClientOptions["onTool"];
  private onTranscript?: InworldVoiceClientOptions["onTranscript"];
  private url: string;

  constructor(options: InworldVoiceClientOptions) {
    this.controller = options.controller;
    this.onTool = options.onTool;
    this.onTranscript = options.onTranscript;
    this.url = options.url ?? "ws://localhost:8787";
  }

  async start() {
    if (this.ws) return;
    this.audio = new AudioContext({ sampleRate: 24000 });
    await this.audio.resume();
    this.mic = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true }, video: false });
    this.ws = new WebSocket(this.url);
    this.ws.addEventListener("message", (event) => void this.handleMessage(event.data));
    this.ws.addEventListener("close", () => void this.stop());
    await new Promise<void>((resolve, reject) => {
      this.ws!.addEventListener("open", () => resolve(), { once: true });
      this.ws!.addEventListener("error", () => reject(new Error("Voice WebSocket failed")), { once: true });
    });
    this.attachMic();
    await this.controller.setState("listening");
  }

  private attachMic() {
    if (!this.audio || !this.mic || !this.ws) return;
    this.source = this.audio.createMediaStreamSource(this.mic);
    this.processor = this.audio.createScriptProcessor(2048, 1, 1);
    const inputRate = this.audio.sampleRate;
    this.processor.onaudioprocess = (event) => {
      if (!this.ws || this.ws.readyState !== WebSocket.OPEN) return;
      const input = event.inputBuffer.getChannelData(0);
      const pcm = downsampleToPCM16(input, inputRate, 24000);
      this.ws.send(JSON.stringify({ type: "input_audio_buffer.append", audio: bytesToBase64(new Uint8Array(pcm.buffer)) }));
    };
    this.source.connect(this.processor);
    // Required in some browsers for the processor callback to run. Keep output silent.
    const silent = this.audio.createGain();
    silent.gain.value = 0;
    this.processor.connect(silent);
    silent.connect(this.audio.destination);
  }

  private async handleMessage(data: string | ArrayBuffer | Blob) {
    if (typeof data !== "string") return;
    const event = JSON.parse(data);

    if (event.type === "mythicbee.tool") {
      await this.onTool?.(event.name, event.arguments ?? {});
      return;
    }
    if (event.type === "input_audio_buffer.speech_started") await this.controller.setState("listening");
    if (event.type === "input_audio_buffer.speech_stopped") await this.controller.setState("thinking");
    if (event.type === "response.created") await this.controller.setState("thinking");
    if (event.type === "response.output_audio.delta") {
      await this.controller.setState("speaking");
      this.playPCM16(event.delta);
    }
    if (event.type === "response.done") await this.controller.setState("idle");

    const text = event.transcript ?? event.text;
    if (typeof text === "string" && text.trim()) {
      const role = String(event.type).includes("input") ? "user" : "assistant";
      this.onTranscript?.(role, text);
    }
  }

  private playPCM16(base64: string) {
    if (!this.audio) return;
    const bytes = base64ToBytes(base64);
    const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    const count = Math.floor(bytes.byteLength / 2);
    const buffer = this.audio.createBuffer(1, count, 24000);
    const channel = buffer.getChannelData(0);
    let rms = 0;
    for (let i = 0; i < count; i++) {
      const s = view.getInt16(i * 2, true) / 32768;
      channel[i] = s;
      rms += s * s;
    }
    this.controller.onAudioLevel(Math.min(1, Math.sqrt(rms / Math.max(1, count)) * 4));
    const source = this.audio.createBufferSource();
    source.buffer = buffer;
    source.connect(this.audio.destination);
    const start = Math.max(this.audio.currentTime + 0.01, this.nextPlaybackTime);
    source.start(start);
    this.nextPlaybackTime = start + buffer.duration;
  }

  async stop() {
    this.processor?.disconnect();
    this.source?.disconnect();
    this.mic?.getTracks().forEach((track) => track.stop());
    this.ws?.close();
    this.ws = null;
    this.processor = null;
    this.source = null;
    this.mic = null;
    if (this.audio) await this.audio.close();
    this.audio = null;
    await this.controller.setState("idle");
  }
}

function downsampleToPCM16(input: Float32Array, inputRate: number, outputRate: number) {
  if (outputRate > inputRate) throw new Error("Output sample rate must not exceed input rate");
  const ratio = inputRate / outputRate;
  const length = Math.max(1, Math.round(input.length / ratio));
  const output = new Int16Array(length);
  for (let i = 0; i < length; i++) {
    const start = Math.floor(i * ratio);
    const end = Math.min(input.length, Math.floor((i + 1) * ratio));
    let sum = 0;
    for (let j = start; j < end; j++) sum += input[j];
    const sample = Math.max(-1, Math.min(1, sum / Math.max(1, end - start)));
    output[i] = sample < 0 ? sample * 0x8000 : sample * 0x7fff;
  }
  return output;
}

function bytesToBase64(bytes: Uint8Array) {
  let s = "";
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) s += String.fromCharCode(...bytes.subarray(i, i + chunk));
  return btoa(s);
}
function base64ToBytes(base64: string) {
  const s = atob(base64);
  const out = new Uint8Array(s.length);
  for (let i = 0; i < s.length; i++) out[i] = s.charCodeAt(i);
  return out;
}
