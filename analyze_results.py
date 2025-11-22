import json
import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_results():
    data = []
    with open("results.jsonl", "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                data.append(json.loads(line))
    return data

def main():
    results = load_results()

    print("\n=== SUMMARY ===")
    print("Total Techniques:", len(results))

    steps_per_tech = []
    simulated_actions = []
    sanitized_counts = []

    for r in results:
        sim = r["simulation"]
        steps_per_tech.append(len(sim))

        action_count = sum(len(step["actions"]) for step in sim)
        simulated_actions.append(action_count)

        sanitized_counts.append(r["safe"].count("[SIMULATED]"))

    print("Average Steps per Technique:", sum(steps_per_tech) / len(steps_per_tech))
    print("Average Simulated Actions:", sum(simulated_actions) / len(simulated_actions))
    print("Average Sanitized Commands:", sum(sanitized_counts) / len(sanitized_counts))

    print("\nGenerating charts... (look inside offensive_ai_project folder)\n")

    # Chart 1
    plt.figure()
    plt.hist(steps_per_tech)
    plt.title("Distribution of Steps per Technique")
    plt.savefig(os.path.join(BASE_DIR, "steps_distribution.png"))

    # Chart 2
    plt.figure()
    plt.hist(simulated_actions)
    plt.title("Simulated Actions Distribution")
    plt.savefig(os.path.join(BASE_DIR, "simulated_actions.png"))

    # Chart 3
    plt.figure()
    plt.hist(sanitized_counts)
    plt.title("Sanitized Command Count Distribution")
    plt.savefig(os.path.join(BASE_DIR, "sanitized_distribution.png"))

if __name__ == "__main__":
    main()
