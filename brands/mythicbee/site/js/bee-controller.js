/**
 * MythicBee Character Controller — Production Version
 * Drives Bartholomew the bee using CSS animations + JS events
 * 
 * States: IDLE → FLY → LAND → LISTEN → TALK → REACT → CELEBRATE
 * Controls: wing flutter, eye tracking, mouth movement, page flight
 */

class MythicBeeController {
  constructor() {
    this.state = "idle";
    this.beeEl = null;
    this.stateListeners = [];
    this.mousePosition = { x: 0, y: 0 };
    this.isFlying = false;
    this.flightPath = [];
  }

  init() {
    this.beeEl = document.getElementById("mythic-bee");
    if (!this.beeEl) {
      console.log("MythicBee: No bee element found.");
      return;
    }
    
    // Entrance animation
    this.flyIn();
    
    // Click handler
    this.beeEl.addEventListener("click", () => this.onBeeClick());
    
    // Mouse tracking for eye follow
    document.addEventListener("mousemove", (e) => {
      this.mousePosition = { x: e.clientX, y: e.clientY };
      if (this.state === "idle") this.lookAtMouse();
    });
    
    // Scroll-triggered reactions
    this.setupScrollReactions();
    
    console.log("MythicBee: Controller initialized");
  }

  // ── State Machine ──────────────────────────────────────────────────

  setState(newState) {
    const old = this.state;
    this.state = newState;
    this.beeEl.className = `bee-character bee--${newState}`;
    this.stateListeners.forEach(fn => fn(newState, old));
  }

  onStateChange(fn) {
    this.stateListeners.push(fn);
  }

  // ── Animations ─────────────────────────────────────────────────────

  flyIn() {
    this.setState("flying_in");
    this.beeEl.style.transform = "translate(100vw, 100vh) scale(0.3)";
    this.beeEl.style.opacity = "0";
    
    requestAnimationFrame(() => {
      this.beeEl.style.transition = "transform 1.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.5s";
      this.beeEl.style.transform = "translate(0, 0) scale(1)";
      this.beeEl.style.opacity = "1";
    });
    
    setTimeout(() => {
      this.setState("idle");
      this.startHover();
    }, 1500);
  }

  startHover() {
    if (this.state !== "idle") return;
    this.beeEl.style.animation = "bee-hover 2.5s ease-in-out infinite";
  }

  flyTo(elementSelector) {
    const target = document.querySelector(elementSelector);
    if (!target || this.isFlying) return;
    
    this.isFlying = true;
    this.setState("flying");
    this.beeEl.style.animation = "none";
    
    const rect = target.getBoundingClientRect();
    const x = rect.left + rect.width / 2 - 60;
    const y = rect.top + rect.height / 2 - 60;
    
    this.beeEl.style.transition = "transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1)";
    this.beeEl.style.transform = `translate(${x}px, ${y}px) scale(1.2) rotate(-15deg)`;
    
    setTimeout(() => {
      this.beeEl.style.transform = `translate(${x}px, ${y}px) scale(1) rotate(0deg)`;
      this.setState("landed");
      this.isFlying = false;
    }, 800);
  }

  celebrate() {
    this.setState("celebrating");
    this.beeEl.style.animation = "none";
    requestAnimationFrame(() => {
      this.beeEl.style.animation = "bee-celebrate 0.6s";
    });
    setTimeout(() => {
      this.setState("idle");
      this.startHover();
    }, 600);
  }

  lookAtMouse() {
    if (!this.beeEl || this.state !== "idle") return;
    const rect = this.beeEl.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = this.mousePosition.x - cx;
    const angle = Math.max(-10, Math.min(10, dx * 0.02));
    this.beeEl.style.transform = `rotate(${angle}deg)`;
  }

  setupScrollReactions() {
    const cta = document.querySelector('[data-action="open-creation"]');
    if (cta) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && this.state === "idle") {
            this.lookAt(cta);
          }
        });
      }, { threshold: 0.5 });
      observer.observe(cta);
    }
  }

  lookAt(element) {
    if (!element || !this.beeEl) return;
    const rect = element.getBoundingClientRect();
    const beeRect = this.beeEl.getBoundingClientRect();
    const dx = (rect.left + rect.width/2) - (beeRect.left + beeRect.width/2);
    const angle = Math.max(-15, Math.min(15, dx * 0.03));
    this.beeEl.style.transform = `rotate(${angle}deg)`;
  }

  onBeeClick() {
    this.celebrate();
    document.dispatchEvent(new CustomEvent("mythicbee:click", { 
      detail: { state: this.state, timestamp: Date.now() } 
    }));
  }
}

// Auto-init
if (typeof window !== "undefined") {
  document.addEventListener("DOMContentLoaded", () => {
    window.mythicBee = new MythicBeeController();
    window.mythicBee.init();
  });
}

export default MythicBeeController;

// ── Character Image Swap ────────────────────────────────────────────

MythicBeeController.prototype.setPose = function(pose) {
  if (!this.beeEl) return;
  const img = this.beeEl.querySelector("img");
  if (!img) return;
  
  const poses = {
    idle: "assets/bartholomew/bartholomew-02.png",
    thinking: "assets/bartholomew/bartholomew-03.png",
    excited: "assets/bartholomew/bartholomew-04.png",
    talking: "assets/bartholomew/bartholomew-04.png",
    celebrating: "assets/bartholomew/bartholomew-04.png",
    flying: "assets/bartholomew/bartholomew-02.png",
  };
  
  if (poses[pose]) {
    img.src = poses[pose];
  }
};

// Patch setState to also swap pose
const originalSetState = MythicBeeController.prototype.setState;
MythicBeeController.prototype.setState = function(newState) {
  originalSetState.call(this, newState);
  this.setPose(newState);
};
