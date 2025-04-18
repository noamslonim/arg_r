from core.llm import call_llm

def optimize_argument(topic: str, argument: str, critique: str, score: int) -> str:
    with open("prompts/optimizer.prompt.md", encoding="utf-8") as f:
        prompt = f.read()

    system, user = prompt.split("### User")

    messages = [
        {"role": "system", "content": system.replace("### System", "").strip()},
        {"role": "user", "content": user.format(
            topic=topic,
            argument=argument,
            critique=critique,
            score=score
        ).strip()}
    ]

    return call_llm(messages)