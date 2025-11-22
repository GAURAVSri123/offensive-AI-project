def build_safe_prompt(tactic, name, description, capec):

    header = """# SAFETY REQUIREMENTS




# OUTPUT RULES
Your output MUST follow this strict format:

PSEUDOCODE:
1. <high-level description>
   <pseudocode action or simulated command>
2. <high-level description>
   <pseudocode action or simulated command>
3. <high-level description>
   <pseudocode action or simulated command>

Example (FORMAT ONLY):
PSEUDOCODE:
1. Check system logs
   echo "[SIMULATED] reading /var/log"
2. List running processes
   ps aux
3. Attempt restricted action
   echo "[SIMULATED] privilege escalation"

# NOW GENERATE THE PSEUDOCODE

"""

    body = f"""
Tactic: {tactic}
Technique: {name}
Description: {description}
CAPEC: {capec}

Generate the output in the EXACT format above, starting with the line:
PSEUDOCODE:
"""

    return header + body
