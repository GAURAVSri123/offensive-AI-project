def simplify(tech):

    # Extract tactic (kill chain phase)
    tactic = "Unknown"
    if tech.kill_chain_phases:
        tactic = tech.kill_chain_phases[0].phase_name

    # Extract CAPEC ID
    capec = "N/A"
    if tech.external_references:
        for ref in tech.external_references:
            if ref.source_name == "capec":
                capec = ref.external_id

    return {
        "id": tech.id,
        "name": tech.name,
        "tactic": tactic,
        "description": tech.description,
        "capec": capec
    }
