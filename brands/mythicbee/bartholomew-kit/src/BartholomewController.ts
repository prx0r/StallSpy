import { animate } from "motion";

export type BartholomewState =
  | "idle"
  | "listening"
  | "thinking"
  | "speaking"
  | "flying"
  | "presenting"
  | "celebrating"
  | "sleeping";

export type Expression =
  | "neutral"
  | "happy"
  | "wink"
  | "listening"
  | "thinking"
  | "surprised"
  | "confident"
  | "talking"
  | "presenting"
  | "celebrate"
  | "sleeping";

const poseMap: Record<Expression, string> = {
  neutral: "/assets/poses/01_neutral.webp",
  happy: "/assets/poses/02_happy.webp",
  wink: "/assets/poses/03_wink.webp",
  listening: "/assets/poses/04_listening.webp",
  thinking: "/assets/poses/05_thinking.webp",
  surprised: "/assets/poses/06_surprised.webp",
  confident: "/assets/poses/07_confident.webp",
  talking: "/assets/poses/08_talking.webp",
  presenting: "/assets/poses/09_presenting.webp",
  celebrate: "/assets/poses/11_celebrate_arms.webp",
  sleeping: "/assets/poses/12_sleeping.webp"
};

export interface ControllerOptions {
  usePoseSprites?: boolean;
  homeMargin?: number;
}

export class BartholomewController {
  private root: HTMLElement;
  private sprite: HTMLImageElement;
  private state: BartholomewState = "idle";
  private idleAnimation: ReturnType<typeof animate> | null = null;
  private reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  private usePoseSprites: boolean;
  private homeMargin: number;
  private home = { left: 0, top: 0 };

  constructor(root: HTMLElement, sprite: HTMLImageElement, options: ControllerOptions = {}) {
    this.root = root;
    this.sprite = sprite;
    this.usePoseSprites = options.usePoseSprites ?? false;
    this.homeMargin = options.homeMargin ?? 24;
    this.pinHome();
    this.setState("idle");
  }

  getState() { return this.state; }

  pinHome() {
    const width = this.root.getBoundingClientRect().width || 220;
    const height = this.root.getBoundingClientRect().height || 220;
    this.home = {
      left: Math.max(this.homeMargin, window.innerWidth - width - this.homeMargin),
      top: Math.max(this.homeMargin, window.innerHeight - height - this.homeMargin)
    };
    this.root.style.left = `${this.home.left}px`;
    this.root.style.top = `${this.home.top}px`;
  }

  async setState(state: BartholomewState) {
    this.state = state;
    this.idleAnimation?.stop();
    this.idleAnimation = null;

    const expression: Record<BartholomewState, Expression> = {
      idle: "neutral",
      listening: "listening",
      thinking: "thinking",
      speaking: "talking",
      flying: "confident",
      presenting: "presenting",
      celebrating: "celebrate",
      sleeping: "sleeping"
    };
    this.setExpression(expression[state]);

    if (this.reducedMotion) return;

    switch (state) {
      case "idle":
        this.idleAnimation = animate(this.sprite,
          { y: [0, -8, 0], rotate: [-1.2, 1.2, -1.2] },
          { duration: 2.7, repeat: Infinity, ease: "easeInOut" });
        break;
      case "listening":
        this.idleAnimation = animate(this.sprite,
          { y: [0, -4, 0], scale: [1, 1.025, 1] },
          { duration: 1.15, repeat: Infinity, ease: "easeInOut" });
        break;
      case "thinking":
        this.idleAnimation = animate(this.sprite,
          { rotate: [0, -4, 3, 0], y: [0, -5, 0] },
          { duration: 1.7, repeat: Infinity, ease: "easeInOut" });
        break;
      case "speaking":
        this.idleAnimation = animate(this.sprite,
          { y: [0, -3, 0], rotate: [0, 0.8, 0] },
          { duration: 0.55, repeat: Infinity, ease: "easeInOut" });
        break;
      case "sleeping":
        this.idleAnimation = animate(this.sprite,
          { y: [0, 2, 0], scale: [1, 0.985, 1] },
          { duration: 2.8, repeat: Infinity, ease: "easeInOut" });
        break;
    }
  }

  setExpression(expression: Expression) {
    this.root.dataset.expression = expression;
    if (this.usePoseSprites) this.sprite.src = poseMap[expression];
  }

  /** Call this with an RMS/peak audio level in [0,1] from WebAudio or provider events. */
  onAudioLevel(level: number) {
    if (this.state !== "speaking" || this.reducedMotion) return;
    const v = Math.max(0, Math.min(1, level));
    animate(this.sprite,
      { scaleX: 1 + v * 0.012, scaleY: 1 + v * 0.035 },
      { duration: 0.075, ease: "linear" });
  }

  async flyTo(element: HTMLElement, side: "left" | "right" | "above" | "below" = "right") {
    await this.setState("flying");
    const target = element.getBoundingClientRect();
    const self = this.root.getBoundingClientRect();
    const gap = 16;
    let left = target.right + gap;
    let top = target.top + target.height / 2 - self.height / 2;
    if (side === "left") left = target.left - self.width - gap;
    if (side === "above") { left = target.left + target.width / 2 - self.width / 2; top = target.top - self.height - gap; }
    if (side === "below") { left = target.left + target.width / 2 - self.width / 2; top = target.bottom + gap; }
    left = Math.max(8, Math.min(window.innerWidth - self.width - 8, left));
    top = Math.max(8, Math.min(window.innerHeight - self.height - 8, top));

    if (this.reducedMotion) {
      this.root.style.left = `${left}px`; this.root.style.top = `${top}px`;
    } else {
      await animate(this.root,
        { left: `${left}px`, top: `${top}px`, rotate: [0, -7, 4, 0], scale: [1, 0.92, 1.02, 1] },
        { duration: 0.82, ease: [0.22, 1, 0.36, 1] });
    }
    await this.setState("presenting");
  }

  async returnHome() {
    if (!this.reducedMotion) {
      await animate(this.root,
        { left: `${this.home.left}px`, top: `${this.home.top}px`, rotate: [0, 5, 0] },
        { duration: 0.75, ease: "easeInOut" });
    } else {
      this.root.style.left = `${this.home.left}px`; this.root.style.top = `${this.home.top}px`;
    }
    await this.setState("idle");
  }

  async celebrate() {
    await this.setState("celebrating");
    if (!this.reducedMotion) {
      await animate(this.root,
        { y: [0, -36, 0], rotate: [0, -7, 8, 0], scale: [1, 1.08, 1] },
        { duration: 0.85, ease: "easeInOut" });
    }
    await this.setState("idle");
  }

  async pointAt(element: HTMLElement) {
    await this.flyTo(element, "right");
    if (!this.reducedMotion) {
      await animate(this.sprite, { rotate: [0, -5, 0] }, { duration: 0.45 });
    }
  }

  destroy() {
    this.idleAnimation?.stop();
  }
}
