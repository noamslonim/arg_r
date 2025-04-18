from core.llm import call_llm, load_prompt_file

def score_improvement(topic: str, prev_argument: str, prev_score: int, new_argument: str) -> int:
    system_prompt, user_prompt_template = load_prompt_file("prompts/delta_scorer.prompt.md")

    user_prompt = user_prompt_template.format(
        topic=topic,
        prev_argument=prev_argument,
        prev_score=prev_score,
        new_argument=new_argument
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = call_llm(messages)
    try:
        return int(response.strip())
    except ValueError:
        raise ValueError(f"Could not parse a valid integer score from response: {response}")