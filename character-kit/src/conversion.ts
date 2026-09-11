// Conversion copy — creation/activation, never "Buy". No "mint" (crypto).
export const COPY = {
  create: "Create this Pog",
  bringToLife: (name: string) => `Bring ${name} to life`,
  alive: (name: string) => `${name} is alive.`,
  portal: "Give it a physical portal",
  bindCard: (name: string) => `Bind ${name} to a card`,
  summon: "Summon",
  send: "Send",
} as const;
