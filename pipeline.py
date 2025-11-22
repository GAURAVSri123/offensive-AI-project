from load_attack import load_attack_dataset
from simplify import simplify
from generate_llm_code import process_entry
from simulator import simulate_output
from tqdm import tqdm
import json
import time

BATCH_SIZE = 1  # process 5 techniques at once

def main():
    techniques = load_attack_dataset()
    simplified_entries = [simplify(t) for t in techniques]

    print("\nRunning pipeline...")

    batch = []

    for entry in tqdm(simplified_entries[:5]):  # limit for speed (test 50)
        batch.append(entry)

        if len(batch) == BATCH_SIZE:
            for item in batch:
                result = process_entry(item)
                simulated = simulate_output(result["safe"])
                result["simulation"] = simulated

                with open("results.jsonl", "a") as f:
                    f.write(json.dumps(result) + "\n")

                print("Generated:", item["name"])

            batch = []  # clear batch

    print("\nPipeline completed!")
    time.sleep(0.5)

if __name__ == "__main__":
    main()
