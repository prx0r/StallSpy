import type { BartholomewController } from "./BartholomewController";

/**
 * Connect any HTMLAudioElement carrying Bartholomew's speech to the mascot.
 * For WebRTC/WebAudio streams, create a MediaStreamSource instead and pass it
 * through the same analyser logic.
 */
export function attachAudioReactiveMouth(audio: HTMLAudioElement, controller: BartholomewController) {
  const context = new AudioContext();
  const source = context.createMediaElementSource(audio);
  const analyser = context.createAnalyser();
  analyser.fftSize = 256;
  source.connect(analyser);
  analyser.connect(context.destination);
  const data = new Uint8Array(analyser.fftSize);
  let raf = 0;

  const tick = () => {
    analyser.getByteTimeDomainData(data);
    let sum = 0;
    for (const sample of data) {
      const n = (sample - 128) / 128;
      sum += n * n;
    }
    controller.onAudioLevel(Math.min(1, Math.sqrt(sum / data.length) * 3.2));
    raf = requestAnimationFrame(tick);
  };
  tick();

  return () => {
    cancelAnimationFrame(raf);
    source.disconnect();
    analyser.disconnect();
    void context.close();
  };
}
