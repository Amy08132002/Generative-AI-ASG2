# Asg2 - Ruoxuan Huang
## Meeting Notes to Action Items Generator

A Python prototype that uses Google Gemini to automatically convert raw meeting notes into structured action items.

### Business Workflow
- **Workflow**: Meeting notes summarization and action item extraction
- **User**: Project managers, team leads, or executive assistants
- **Input**: Raw meeting notes or transcript (plain text)
- **Output**: A structured summary with clear action items, owners, and deadlines
- **Why automate**: After every meeting, someone manually reads through notes and extracts tasks. This is repetitive and error-prone. An LLM can do this in seconds, ensuring nothing is missed and output is consistent across all meetings.

### Project Structure
- README.md
- app.py
- prompts.md
- eval_set.json
- report.md
- outputs/

### Setup & Usage

1. Install dependencies
pip install google-genai

2. Set your Gemini API key
$env:GEMINI_API_KEY="your_api_key_here"

3. Run the app
python app.py

Results are saved to the outputs/ folder.

### Video Walkthrough
📹 [[Add YouTube link here after recording](https://youtu.be/Nn00l9hQm1Q)]
