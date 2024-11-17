from atackSchema import attacks

def attack_location(technique):
    if technique in attacks:
      return attacks[technique]

    return "Unknown"

print(attack_location("arm_attack"))