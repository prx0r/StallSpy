#!/usr/bin/env python3
"""
OpenCode LLM Adapter — calls opencode run with mimo-v2.5
and parses structured JSON output.
"""
import json
import subprocess
import os
from pathlib import Path

OPENCODE = "/root/.opencode/bin/opencode"

def call_opencode(prompt: str, system: str = "", timeout: int = 60) -> dict:
    """Call opencode run and parse JSON response."""
    full_prompt = prompt
    if system:
        full_prompt = f"{system}\n\n{prompt}"
    
    try:
        result = subprocess.run(
            [OPENCODE, "run", full_prompt],
            capture_output=True, text=True, timeout=timeout,
            cwd="/root/StallShark"
        )
        output = result.stdout.strip()
        
        # Extract JSON from output (opencode adds terminal formatting)
        # Find the last JSON object in the output
        lines = output.split("\n")
        for line in reversed(lines):
            line = line.strip()
            if line.startswith("{"):
                try:
                    return json.loads(line)
                except json.JSONDecodeError:
                    continue
        
        # Try to find JSON anywhere in output
        import re
        matches = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', output)
        for m in reversed(matches):
            try:
                return json.loads(m)
            except json.JSONDecodeError:
                continue
        
        # Fallback: return raw text
        return {"raw": output, "error": "no_json_found"}
    
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "raw": ""}
    except Exception as e:
        return {"error": str(e), "raw": ""}

def call_opencode_text(prompt: str, system: str = "", timeout: int = 60) -> str:
    """Call opencode run and return raw text."""
    full_prompt = prompt
    if system:
        full_prompt = f"{system}\n\n{prompt}"
    
    try:
        result = subprocess.run(
            [OPENCODE, "run", full_prompt],
            capture_output=True, text=True, timeout=timeout,
            cwd="/root/StallShark"
        )
        # Clean terminal formatting
        output = result.stdout.strip()
        lines = output.split("\n")
        # Skip status lines (starting with [ or >)
        clean = []
        for line in lines:
            if not line.startswith("[") and not line.startswith("> ") and line.strip():
                clean.append(line.strip())
        return "\n".join(clean) if clean else output
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print("=== OpenCode LLM Adapter Test ===\n")
    
    # Test 1: Simple text
    print("1. Text response:")
    text = call_opencode_text("Say hello in 5 words")
    print(f"   {text}\n")
    
    # Test 2: JSON structured output
    print("2. JSON response:")
    json_out = call_opencode('{"message": "greeting", "confidence": 0.9}')
    print(f"   {json.dumps(json_out, indent=2)}\n")
    
    # Test 3: Complex structured output
    print("3. Complex SubjectiveState:")
    state = call_opencode("""Return ONLY a JSON object:
{
  "objective_today": "what to do today",
  "bottleneck": "main blocker",
  "confidence": 0.5,
  "biggest_concern": "main worry",
  "biggest_excitement": "main excitement"
}
Business state: Day 5, $88 cash, 0 revenue, 0 listings, working on specs.""")
    print(f"   {json.dumps(state, indent=2)}\n")
    
    print("=== All working ===")
