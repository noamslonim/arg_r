from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from agents import chat
from agents import critic
from agents import scorer
from agents import optimizer
from agents import delta_scorer

topic = chat.choose_topic()
print(f"\nSelected topic:\n→ {topic}\n")

argument = chat.get_initial_argument(topic)
print(f"\nInitial argument:\n→ {argument}\n")

critique = critic.critique_argument(argument, topic)
print("\nCritique:")
print("➜", critique)

score = scorer.score_argument(argument, critique, topic)
print("\nScore:")
print("➜", score)

improved_argument = optimizer.optimize_argument(topic, argument, critique, score)
print("\nImproved Argument:")
print("→", improved_argument)

new_score = delta_scorer.score_improvement(
    topic=topic,
    prev_argument=argument,
    prev_score=score,
    new_argument=improved_argument
)

print("\nNew Score:")
print("→", new_score)




