#!/bin/bash
# Generate multiple 3D model variations from Forge API

PROMPTS=(
  "stylized anime bee warrior, gold armor, purple gem eyes, four translucent wings, red cape, black antennae, heroic pose, clean topology"
  "cute chibi bee character, oversized head, gold and black stripes, big purple eyes, small red cape, kawaii style, low-poly"
  "premium collectible bee figurine, metallic gold, translucent wings, purple eyes, flowing red cape, studio lighting"
  "pixel art bee character, 16-bit style, gold body, black stripes, tiny wings, retro game aesthetic"
  "mechanical steampunk bee, brass gears, copper wings, Victorian style, detailed craftsmanship"
  "cyberpunk neon bee, glowing wings, electric blue accents, futuristic armor, holographic effects"
  "art nouveau bee, ornate gold patterns, flowing lines, decorative wings, elegant pose"
  "comic book superhero bee, bold outlines, dynamic pose, dramatic lighting, cape flowing"
  "paper craft bee, origami style, folded paper textures, geometric shapes, low-poly"
  "glass crystal bee, transparent body, refractions, prismatic wings, light effects"
)

for i in "${!PROMPTS[@]}"; do
  echo "Generating model $((i+1))/10..."
  RESULT=$(curl -s "https://three.ws/api/forge" \
    -H "Content-Type: application/json" \
    -d "{\"prompt\":\"${PROMPTS[$i]}\"}" 2>&1)
  JOB_ID=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('job_id','NONE'))" 2>/dev/null)
  echo "  Job: $JOB_ID"
done

echo "All jobs submitted. Polling..."
