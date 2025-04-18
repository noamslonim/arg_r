from core.llm import call_llm

def prompt_user(prompt: str) -> str:
    return input(prompt).strip()

def load_prompt(filepath: str) -> tuple[str, str]:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    system, user = content.split("### User")
    return system.replace("### System", "").strip(), user.strip()

def choose_topic() -> str:
    choice = prompt_user("Do you want to suggest a debatable topic? (yes/no): ").lower()

    if choice.startswith("y"):
        return prompt_user("Please enter your debatable topic: ")

    system, user = load_prompt("prompts/topic_suggestion.prompt.md")

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    return call_llm(messages)

def get_initial_argument(topic: str) -> str:
    choice = prompt_user("Do you want to write the initial argument? (yes/no): ").lower()

    if choice.startswith("y"):
        return prompt_user("Please enter your argument supporting this topic: ")

    system, user = load_prompt("prompts/initial_argument.prompt.md")

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user.format(topic=topic)}
    ]
    return call_llm(messages)