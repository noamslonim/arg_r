# 🧠 Argument Refinement Loop

An interactive tool that uses LLMs to iteratively improve arguments on debatable topics.

---

## 🚀 Features

- 📌 Topic selection: choose or generate a clear debatable question.
- ✍️ Argument drafting: write your own argument or get one suggested.
- 🔍 Critique: receive a focused critique on the argument’s biggest weakness.
- 🔁 Iterative improvement: revise the argument in response to the critique.
- 📊 Scoring: evaluate argument quality on a 0–100 scale using a strict rubric.
- 🧠 Memory: tracks the best-scoring version so far across multiple iterations.
- 🎯 Goal: improve the argument until no further gains are made — or you decide to stop.

---

## 🛠️ Requirements

- Python 3.10+
- OpenAI API key

Install dependencies:

```bash
pip install -r requirements.txt
Set your OpenAI key as an environment variable (recommended) or in a .env file:

export OPENAI_API_KEY=your-key-here
🧪 Running the Loop
Run the interactive session from your terminal:

python main.py
You’ll be guided through topic selection, argument generation, critique, scoring, and refinement. At any point, you can choose to continue or exit.

📁 Project Structure
.
├── agents/                    # Modular agents for each task (chat, critique, optimizer, etc.)
│   ├── chat.py
│   ├── critic.py
│   ├── optimizer.py
│   └── single_arg_scorer.py
├── prompts/                   # Markdown-formatted prompt files
│   └── *.prompt.md
├── core/
│   └── llm.py                 # Handles LLM calls and prompt loading
├── main.py                    # Entry point for the iterative loop
├── requirements.txt
└── README.md
📌 Notes
This project is modular by design — feel free to extend or swap out agents (e.g., for multi-argument scoring, alternate LLMs, or new domains).

Prompts are editable Markdown files in the prompts/ directory — customize them to fine-tune behavior.

Arguments are scored strictly, with an emphasis on clarity, logic, and evidence.

🤝 Contributing
Pull requests, feature ideas, and feedback are welcome. Open an issue or fork the repo to try new ideas!

📜 License
MIT License

🙌 Acknowledgments
Built with OpenAI and Cursor.