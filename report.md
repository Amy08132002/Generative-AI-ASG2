# Report: Meeting Notes to Action Items Generator

**Author:** Ruoxuan Huang
**Model:** Google Gemini 3 Flash Preview (via Gemini API)
**Assignment:** Week 2 — Build and Evaluate a Simple GenAI Workflow

---

## Business Use Case

After every meeting, someone on the team manually reads through notes and extracts tasks, owners, and deadlines. This process is time-consuming, inconsistent across team members, and prone to missing items. This prototype uses Gemini to automatically convert raw meeting notes into a structured summary with action items, decisions, and follow-up questions — reducing the time spent on post-meeting documentation and improving consistency.

The target user is a project manager, team lead, or executive assistant who receives raw notes and needs to distribute a clean action item list to the team.

---

## Model Choice

I used **Gemini 3 Flash Preview** via Google AI Studio. It is fast, free to access at the API level, and performs well on structured extraction tasks. The model handles varied input lengths well and follows formatting instructions reliably once the prompt is specific enough.

---

## Baseline vs. Final Design

| Dimension | Version 1 (Baseline) | Version 3 (Final) |
|---|---|---|
| Output format | Inconsistent — sometimes bullets, sometimes prose | Consistent structured format every run |
| Hallucination (Case 05) | Invented owners, dates, dollar amounts | Marks unknown fields as TBD |
| Vague notes (Case 03) | Made up plausible-sounding tasks | Correctly flags notes as too vague |
| Missing owners | Sometimes invented names | Consistently writes "TBD" |
| Open questions | Not captured | Surfaced in FOLLOW-UP QUESTIONS section |

The most impactful prompt change was adding the explicit rule: "Do NOT invent owners, dates, or tasks that are not in the notes." This directly addressed the hallucination risk in Cases 03 and 05.

---

## Where the Prototype Still Fails

Three failure modes remain. First, when meeting notes are extremely sparse (Case 05), the model sometimes produces a confident-sounding summary even though there is almost no real information to work with — the tone can mislead a reader into thinking more was decided than actually was. Second, the model has no way to verify names — if notes say "Sarah will handle it" but the team has two people named Sarah, the model cannot flag this ambiguity. Third, the model cannot distinguish between a decision that was finalized and one that was still being discussed, unless the notes are explicit about this.

---

## Deployment Recommendation

**Deploy as a drafting tool with mandatory human review, not as an autonomous system.**

The prototype reliably produces a useful first draft of action items for well-structured meeting notes. It saves time and raises the baseline quality of post-meeting documentation. However, it should not send action item emails or update project management tools automatically. The hallucination risk on vague inputs and the inability to verify names or distinguish tentative from final decisions mean that a human must review every output before it is distributed to a team. Under a human-in-the-loop model, this prototype is worth deploying and continuing to develop.
