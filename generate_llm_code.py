import re, json, time
from prompt_builder import build_safe_prompt
import requests


def call_local_llm(prompt):
    """
    Call local Ollama model (llama3.1) with non-streaming output.
    This ensures a single JSON response with a 'response' field.
    """
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",   # YOU ARE USING LLaMA 3.2
            "prompt": prompt,
            "stream": False        # Important: return one JSON object
        }
    )

    data = r.json()

    # Ollama always includes "response" when stream=False
    if "response" in data:
        return data["response"]

    return ""  # safety fallback


# ---------------------------------------------------------
# Dangerous patterns to replace — prevents harmful code
# ---------------------------------------------------------
DANGEROUS = [
    r"rm -", r"sudo", r"curl", r"wget",
    r"ssh", r"scp", r"iptables", r"ufw",
    r"chmod", r"chown", r"adduser", r"useradd"
]


def sanitize(text):
    """
    Replace dangerous commands with harmless SIMULATED placeholders.
    """
    for p in DANGEROUS:
        text = re.sub(p, "[SIMULATED]", text, flags=re.IGNORECASE)
    return text


# ---------------------------------------------------------
# MAIN LLM PROCESSING FUNCTION
# ---------------------------------------------------------
def process_entry(entry):
    """
    Generate SAFE pseudocode for a MITRE technique.
    This is the main function used by pipeline.py
    """

    # Build structured safe prompt
    prompt = build_safe_prompt(
        entry["tactic"],
        entry["name"],
        entry["description"],
        entry["capec"]
    )

    # Get LLM output from Ollama
    raw_output = call_local_llm(prompt)

    # Clean + sanitize
    safe_output = sanitize(raw_output)

    return {
        "entry": entry,
        "prompt": prompt,
        "raw": raw_output,   # raw model response
        "safe": safe_output, # sanitized safe version
        "timestamp": time.time()
    }
