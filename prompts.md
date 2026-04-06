# Prompt Iteration Log

## Version 1 — Initial Prompt

```
You are a helpful assistant. Read the meeting notes and extract the action items.
```

**What changed:** This was the starting point — minimal instruction with no output format, no constraints, and no guidance on how to handle missing information.

**Result:** The model produced inconsistent output. Sometimes it returned bullet points, sometimes paragraphs. In Case 03 (vague notes), it invented fictional owners and deadlines not present in the input. In Case 05 (hallucination test), it fabricated specific dollar amounts and assigned names to tasks that had no owners mentioned. The output was not structured enough to be usable in a real workflow.

---

## Version 2 — Revision 1: Add structured output format

```
You are a meeting assistant. Read the meeting notes and return a structured summary using this format:

MEETING SUMMARY:
[Brief summary]

ACTION ITEMS:
- [ ] [Task] | Owner: [Name] | Due: [Date]

DECISIONS MADE:
- [Decisions]

Guidelines:
- Be concise
- Only include what is in the notes
```

**What changed:** Added a strict output format so results are consistent and machine-readable. Added a guideline to only use information from the notes.

**What improved:** Output format became consistent across all cases. Case 01 and Case 02 (normal cases) produced clean, well-structured results. The structured format made it easy to compare outputs across runs.

**What stayed the same or got worse:** Case 03 and Case 05 still showed hallucination — the model continued to assign "TBD" inconsistently and sometimes still invented plausible-sounding owners. There was no explicit instruction on what to do when information is missing.

---

## Version 3 — Revision 2: Add anti-hallucination rules and missing-info handling

```
You are an expert meeting facilitator and project coordinator.
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
```

**What changed:** Added two critical rules:
1. Explicit instruction NOT to invent owners, dates, or tasks.
2. Clear fallback behavior — write "TBD" when information is missing, and explicitly flag when notes are too vague.
Also added a FOLLOW-UP QUESTIONS section to capture unresolved items.

**What improved:** Case 03 (vague notes) now correctly states that the notes are too vague and avoids fabricating tasks. Case 05 (hallucination test) improved significantly — the model marks all owners and dates as TBD instead of inventing them. The FOLLOW-UP QUESTIONS section helps surface open issues like the HR policy question in Case 04.

**What stayed the same:** Case 05 still occasionally produces an overly confident summary tone even when data is missing. Human review remains necessary before distributing action items to a team.
