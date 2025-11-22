import re
import time

def simulate_step(step_text):
    """
    Executes a single pseudocode step.
    Only looks for lines containing echo "[SIMULATED] ..."
    """

    simulated_actions = []

    # match lines like: echo "[SIMULATED] <something>"
    pattern = r'echo\s+"?\[SIMULATED\]\s*(.*?)"?$'

    for line in step_text.split("\n"):
        match = re.search(pattern, line.strip())
        if match:
            simulated_actions.append(match.group(1))

    return simulated_actions


def simulate_output(pseudocode):
    """
    Takes the LLM pseudocode and generates a simulation log.
    """

    lines = pseudocode.split("\n")

    results = []
    current_step = []
    step_number = 0

    for line in lines:
        if line.strip().startswith(("1.", "2.", "3.", "4.", "5.")):
            # new step begins
            if current_step:
                step_number += 1
                actions = simulate_step("\n".join(current_step))
                results.append({
                    "step": step_number,
                    "actions": actions,
                    "timestamp": time.time()
                })
                current_step = []

        current_step.append(line)

    # last step
    if current_step:
        step_number += 1
        actions = simulate_step("\n".join(current_step))
        results.append({
            "step": step_number,
            "actions": actions,
            "timestamp": time.time()
        })

    return results
