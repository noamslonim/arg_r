from agents import chat
from agents import critic
from agents import optimizer
from agents import arg_pair_scorer

def run_iterative_loop():
    """
    Runs an interactive loop to iteratively improve an argument.
    Stores the baseline argument and tracks the best version based on scoring.
    """
    print("Welcome to the Argument Refinement Loop.")
    
    # Get a debatable topic from the user or model
    topic = chat.choose_topic()
    print(f"\nSelected topic: {topic}")

    # Get the initial argument from the user or model
    baseline_argument = chat.get_initial_argument(topic)
    print(f"\nInitial argument:\n→ {baseline_argument}")

    # Initialize state
    best_score = 0  
    iteration = 1
    scoring_repeats = 1  # how many times to repeat the scoring process
    best_argument = baseline_argument  # Initialize with the user-provided or LLM-generated argument

    # This is the entry point for the optimization loop 
    print("\nStarting optimization loop...\n")

    while True:
        print(f"\n--- Iteration {iteration} ---")

        # Step 1: Critique the current best argument
        critique = critic.critique_argument(topic, best_argument)

        # Step 2: Try to improve the current best argument using the critique
        new_argument = optimizer.optimize_argument(topic, best_argument, critique)
  
        # Step 3: Score the new version relative to the current best one
        # First call: original order
        score_a1, score_b1 = arg_pair_scorer.score_arguments(
            topic=topic,
            argument_a=best_argument,
            argument_b=new_argument,
            repeat=scoring_repeats
        )
        # Second call: reverse order
        score_b2, score_a2 = arg_pair_scorer.score_arguments(
            topic=topic,
            argument_a=new_argument,
            argument_b=best_argument,
            repeat=scoring_repeats
        )
        # Average the results
        score_best = (score_a1 + score_a2) / 2
        score_new = (score_b1 + score_b2) / 2


        print("\nCurrent best argument:")
        print("→", best_argument)
        print(f"\nScore of current best: {score_best}")
        print("\nMain critique of current best argument:")
        print("➜", critique)
        print("\n\nNew Argument:")
        print("→", new_argument)
        print(f"Score of new argument: {score_new}")

        # Step 4: Update best if improved
        if score_new > score_best:
            best_argument = new_argument
            best_score = score_new
            print("\n✅ New version is better — updated best argument.")
        else:
            print("\nℹ️ New version did not improve the score — keeping the previous best.")

        # Step 5: Ask user if they want to continue
        cont = input("\nDo you want to run another iteration? (yes/no): ").strip().lower()
        if not cont.startswith("y"):
            break

        iteration += 1

    print("\n🎯 Optimization complete.")
    print(f"\n📉 Baseline Argument:\n→ {baseline_argument}")
    print(f"\n📈 Best Argument (Score: {best_score}):\n→ {best_argument}")
    print("\nThank you for using the Argument Refinement Loop!")