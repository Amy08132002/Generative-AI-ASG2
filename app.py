"""
app.py - Meeting Notes to Action Items Generator
Uses Google Gemini API to extract structured action items from raw meeting notes.

Usage:
    python app.py

Requirements:
    pip install google-genai
    $env:GEMINI_API_KEY="your_api_key_here"
"""

import os
import json
import datetime
import time
from google import genai

# ── Configuration ──────────────────────────────────────────────────────────────

API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
MODEL_NAME = "gemini-3-flash-preview"

# ── Prompt (edit this to iterate) ─────────────────────────────────────────────

SYSTEM_INSTRUCTION = """You are an expert meeting facilitator and project coordinator.
Your job is to read raw meeting notes and extract a clear, structured summary.

Your output must follow this exact format:

MEETING SUMMARY:
[1-2 sentence summary of the meeting purpose and outcome]

ACTION ITEMS:
- [ ] [Task description] | Owner: [Name or "TBD"] | Due: [Date or "TBD"]

DECISIONS MADE:
- [Any decisions that were finalized during the meeting]

FOLLOW-UP QUESTIONS:
- [Any open questions that were not resolved]

Guidelines:
- Only include action items explicitly mentioned in the notes
- Do NOT invent owners, dates, or tasks that are not in the notes
- If owner or due date is not mentioned, write "TBD"
- Be concise and factual
- If the notes are too vague to extract action items, say so clearly
"""

def generate_summary(meeting_notes: str) -> str:
    """Send meeting notes to Gemini and return structured action items."""
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=meeting_notes,
        config=genai.types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=500,
        )
    )
    return response.text.strip()


def run_eval_set(eval_path: str = "eval_set.json"):
    """Run all test cases from the eval set and save results."""
    with open(eval_path, "r", encoding="utf-8") as f:
        eval_cases = json.load(f)

    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"outputs/results_{timestamp}.txt"

    print(f"Running {len(eval_cases)} eval cases with model: {MODEL_NAME}\n")
    print("=" * 70)

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(f"Model: {MODEL_NAME}\nTimestamp: {timestamp}\n\n")

        for i, case in enumerate(eval_cases, 1):
            print(f"[Case {i}] {case['id']} — {case['type']}")
            print(f"Input:\n{case['input']}\n")

            summary = generate_summary(case["input"])

            print(f"Output:\n{summary}")
            print("-" * 70)

            out.write(f"{'='*70}\n")
            out.write(f"Case {i}: {case['id']} ({case['type']})\n")
            out.write(f"Meeting Notes Input:\n{case['input']}\n\n")
            out.write(f"Expected behavior:\n{case['expected_behavior']}\n\n")
            out.write(f"Generated Output:\n{summary}\n\n")

            time.sleep(3)

    print(f"\n✅ Results saved to: {output_file}")


if __name__ == "__main__":
    run_eval_set("eval_set.json")
