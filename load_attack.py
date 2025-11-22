from mitreattack.stix20 import MitreAttackData

def load_attack_dataset():
    # Load the MITRE STIX file
    mitre = MitreAttackData("enterprise-attack.json")

    # Extract techniques
    techniques = mitre.get_techniques()

    print("Total techniques loaded:", len(techniques))
    return techniques

if __name__ == "__main__":
    load_attack_dataset()
