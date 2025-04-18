from core.llm import call_llm

def load_prompt(filepath: str) -> tuple[str, str]:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    system, user = content.split("### User")
    return system.replace("### System", "").strip(), user.strip()

def critique_argument(topic: str, argument: str) -> str:
    system, user = load_prompt("prompts/critic.prompt.md")

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user.format(topic=topic, argument=argument)}
    ]

    return call_llm(messages)