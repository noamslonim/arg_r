from core.llm import call_llm, load_prompt_file

def score_argument(argument: str, critique: str, topic: str) -> int:
    system_prompt, user_template = load_prompt_file("prompts/scorer.prompt.md")
    
    user_message = user_template.format(
        topic=topic.strip(),
        argument=argument.strip(),
        critique=critique.strip()
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    response = call_llm(messages)

    try:
        return int(response.strip())
    except ValueError:
        raise ValueError(f"Expected an integer score, but got: {response}")
        