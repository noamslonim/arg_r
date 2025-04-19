import re
from core.llm import call_llm, load_prompt_file

def score_arguments(topic: str, argument_a: str, argument_b: str, repeat: int = 1) -> tuple[float, float]:
    """
    Scores two arguments independently with respect to a shared topic, possibly repeating multiple times.

    Args:
        topic: The debate topic.
        argument_a: First argument to evaluate.
        argument_b: Second argument to evaluate.
        repeat: Number of times to repeat the scoring and average the result.

    Returns:
        Tuple (avg_score_a, avg_score_b)
    """
    # Limit repeat to 5 and print a warning if a higher value is provided
    if repeat > 3:
        print(f"Warning: repeat value {repeat} exceeds maximum of 5. Setting repeat to 5.")
        repeat = 3
        
    system_prompt, user_prompt_template = load_prompt_file("prompts/arg_pair_scorer.prompt.md")

    score_list_a, score_list_b = [], []

    for _ in range(repeat):
        user_prompt = user_prompt_template.format(
            topic=topic.strip(),
            argument_a=argument_a.strip(),
            argument_b=argument_b.strip()
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # moving to gpt-3.5-turbo to save costs and speed up response times
        response = call_llm(messages, model="gpt-3.5-turbo", temperature=0.0).strip()

        scores = [int(s) for s in re.findall(r"\b\d{1,3}\b", response)]
        valid_scores = [s for s in scores if 0 <= s <= 100]

        if len(valid_scores) >= 2:
            score_list_a.append(valid_scores[0])
            score_list_b.append(valid_scores[1])
        else:
            raise ValueError(f"Invalid scoring response: {response}")

    avg_a = sum(score_list_a) / repeat
    avg_b = sum(score_list_b) / repeat
    return avg_a, avg_b