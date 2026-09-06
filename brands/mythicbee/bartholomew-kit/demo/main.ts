import "./style.css";
import { BartholomewController } from "../src/BartholomewController";
import { createEmptyGiftBrief, mergeGiftBrief } from "../src/giftBrief";

const root = document.querySelector<HTMLElement>("#bartholomew")!;
const sprite = document.querySelector<HTMLImageElement>("#bartholomew-sprite")!;
sprite.src = new URL("../assets/canonical/bartholomew.webp", import.meta.url).href;

const controller = new BartholomewController(root, sprite, { usePoseSprites: false, homeMargin: 22 });
window.addEventListener("resize", () => controller.pinHome());

for (const button of document.querySelectorAll<HTMLButtonElement>("[data-state]")) {
  button.addEventListener("click", () => void controller.setState(button.dataset.state as any));
}
document.querySelector<HTMLButtonElement>("#fly-demo")!.addEventListener("click", () => {
  void controller.flyTo(document.querySelector<HTMLElement>("#football-film")!, "right");
});
document.querySelector<HTMLButtonElement>("#celebrate-demo")!.addEventListener("click", () => void controller.celebrate());
document.querySelector<HTMLButtonElement>("#home-demo")!.addEventListener("click", () => void controller.returnHome());

const dialog = document.querySelector<HTMLDialogElement>("#chat-dialog")!;
document.querySelector<HTMLButtonElement>("#bee-talk")!.addEventListener("click", () => {
  dialog.showModal();
  void controller.setState("listening");
});
dialog.addEventListener("close", () => void controller.setState("idle"));

let brief = createEmptyGiftBrief();
brief = mergeGiftBrief(brief, {
  occasion: { type: "fathers_day", label: "Father's Day" },
  recipient: { relationship: "dad", age: 60 },
  interests: [{ label: "football", detail: "Liverpool FC", importance: 0.95 }],
  personality: [{ trait: "teasing sense of humour", evidence: "Always taking the piss out of everyone" }],
  confidence: { occasion: 1, recipient: .9, interests: .8, personality: .7 }
});
document.querySelector("#brief-json")!.textContent = JSON.stringify(brief, null, 2);

// Fake speaking amplitude so you can see the audio-reactive hook before wiring voice.
let t = 0;
setInterval(() => {
  if (controller.getState() !== "speaking") return;
  t += .3;
  controller.onAudioLevel((Math.sin(t) + 1) * .35);
}, 80);
