// Generic data-driven loading-copy engine (bee vocab NOT hardcoded).
export type LoadingPhrase = { text: string; themes?: string[]; seasons?: string[]; characters?: string[]; weight?: number };

const PACK: LoadingPhrase[] = [
  { text: "Teaching Buster tax fraud...", characters: ["buster"] },
  { text: "Hiding from Dave next door...", characters: ["buster"] },
  { text: "Locating emergency cheese...", characters: ["buster"] },
  { text: "Polishing wings...", characters: ["bartholomew"] },
  { text: "Consulting the hive...", characters: ["bartholomew"] },
  { text: "Moving glass away from table edge...", characters: ["pickles"] },
  { text: "Giving Kevin administrative privileges...", characters: ["kevin"] },
  { text: "Removing Kevin's administrative privileges...", characters: ["kevin"] },
];

export function phrasesFor(character: string, season?: string): string[] {
  return PACK.filter((p) => (!p.characters || p.characters.includes(character)) && (!season || !p.seasons || p.seasons.includes(season))).map((p) => p.text);
}
