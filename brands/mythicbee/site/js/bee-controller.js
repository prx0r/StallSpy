/**
 * MythicBee Character Controller
 * Drives Bartholomew the bee using Motion.js
 * States: IDLE → FLY → LAND → LISTEN → TALK → REACT → CELEBRATE
 */

import { animate, scroll, inView } from "motion";

class MythicBeeController {
  constructor() {
    this.state = "idle";
    this.beeEl = null;
    this.stateListeners = [];
  }

  init() {
    this.beeEl = document.getElementById("mythic-bee") || document.querySelector(".bee-character");
    if (!this.beeEl) {
      console.log("MythicBee: No bee element found. Add <div id='mythic-bee'> to your page.");
      return;
    }
    
    // Entrance animation on page load
    this.flyIn();
    
    // Click handler
    this.beeEl.addEventListener("click", () => this.onBeeClick());
    
    // Mouse follow (subtle)
    document.addEventListener("mousemove", (e) => this.onMouseMove(e));
    
    console.log("MythicBee: Controller initialized");
  }

  // ── State Transitions ────────────────────────────────────────────────

  flyIn() {
    this.state = "flying_in";
    if (!this.beeEl) return;
    
    // Start off-screen, fly to bottom-right
    animate(this.beeEl, 
      { x: ["100vw", "85vw"], y: ["100vh", "80vh"], opacity: [0, 1] },
      { duration: 1.5, easing: "ease-out" }
    ).then(() => {
      this.state = "idle";
      this.startIdleAnimation();
    });
  }

  startIdleAnimation() {
    if (!this.beeEl) return;
    // Gentle hover
    animate(this.beeEl,
      { y: ["0px", "-8px", "0px"] },
      { duration: 2, repeat: Infinity, easing: "ease-in-out" }
    );
  }

  flyTo(elementSelector) {
    const target = document.querySelector(elementSelector);
    if (!target || !this.beeEl) return;
    
    this.state = "flying";
    const rect = target.getBoundingClientRect();
    
    animate(this.beeEl,
      { 
        x: `${rect.left + rect.width/2}px`,
        y: `${rect.top + rect.height/2}px`,
        scale: [1, 1.2, 1],
        rotate: [0, -15, 0]
      },
      { duration: 0.8, easing: "ease-in-out" }
    ).then(() => {
      this.state = "landed";
    });
  }

  celebrate() {
    if (!this.beeEl) return;
    this.state = "celebrating";
    // Bounce + sparkle
    animate(this.beeEl,
      { scale: [1, 1.3, 0.9, 1.1, 1], rotate: [0, -10, 10, -5, 0] },
      { duration: 0.6 }
    ).then(() => {
      this.state = "idle";
      this.startIdleAnimation();
    });
  }

  lookAt(target) {
    if (!this.beeEl) return;
    // Subtle head tilt toward target
    const rect = target.getBoundingClientRect ? target.getBoundingClientRect() : {left: 0};
    const direction = rect.left > window.innerWidth / 2 ? -5 : 5;
    animate(this.beeEl, { rotate: `${direction}deg` }, { duration: 0.3 });
  }

  pointAt(elementSelector) {
    const target = document.querySelector(elementSelector);
    if (!target || !this.beeEl) return;
    
    this.lookAt(target);
    this.state = "pointing";
  }

  onBeeClick() {
    // Dispatch custom event for the site to handle
    document.dispatchEvent(new CustomEvent("mythicbee:click", { detail: { state: this.state } }));
    this.celebrate();
  }

  onMouseMove(e) {
    if (this.state !== "idle") return;
    // Subtle eye/mouse follow (handled by CSS or Rive later)
  }

  // ── Expression Control ──────────────────────────────────────────────

  setExpression(expr) {
    // Map to CSS classes or Rive inputs
    if (this.beeEl) {
      this.beeEl.className = `bee-character bee--${expr}`;
    }
  }
}

// Auto-init on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  window.mythicBee = new MythicBeeController();
  window.mythicBee.init();
});

export default MythicBeeController;
