from agents import chat
from agents import critic
from agents import optimizer
from agents import single_arg_scorer

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
    iteration = 1
    scoring_repeats = 2  # how many times to repeat the scoring process
    best_score = single_arg_scorer.score_argument(topic, baseline_argument, scoring_repeats)
    best_argument = baseline_argument  # Initialize with the user-provided or LLM-generated argument
    arg_switched = True

    # This is the entry point for the optimization loop 
    print("\nStarting optimization loop...\n")

    while True:
        print(f"\n--- Iteration {iteration} ---")

        # Step 1: Critique the current best argument
        if arg_switched:
            critique = critic.critique_argument(topic, best_argument)
        else:
            critique = critic.critique_argument(topic, best_argument, temperature=1.0, strict=True)
        
        # Step 2: Try to improve the current best argument using the critique
        if arg_switched:
            new_argument = optimizer.optimize_argument(topic, best_argument, critique)
        else:
            new_argument = optimizer.optimize_argument(topic, best_argument, critique, temperature=1.0, strategic_shift=True)
  
        # Step 3: Score the new argument
        new_score = single_arg_scorer.score_argument(topic, new_argument, scoring_repeats)

        print("\nBest argument:")
        print("→", best_argument)
        print(f"Score: {best_score:.1f}")
        print("\nMain critique:")
        print("➜", critique)
        print("\nNew Argument:")
        print("→", new_argument)
        print(f"Score: {new_score:.1f}")

        # Step 4: Update best if improved
        if new_score > best_score:
            best_argument = new_argument
            best_score = new_score
            print("\n✅ New version is better — updated best argument.")
            arg_switched = True
        else:
            print("\nℹ️ New version did not improve the score — keeping the previous best.")
            arg_switched = False

        # Step 5: Ask user if they want to continue
        cont = input("\nDo you want to run another iteration? (yes/no): ").strip().lower()
        if not cont.startswith("y"):
            break

        iteration += 1
        if iteration > 10:
            break
            print("\nExceeded maximum iterations. Exiting.")

    print("\n🎯 Optimization complete.")
    print(f"\n📉 Baseline Argument:\n→ {baseline_argument}")
    print(f"\n📈 Best Argument (Score: {best_score:.1f}):\n→ {best_argument}")
    print("\nThank you for using the Argument Refinement Loop!")