from schema import attacks

class AttackFinder:

    def __init__(self, attack):
        self.attack = attack

    def __call__(self):
        if self.attack not in attacks:
            return "unknown location"
        return attacks[self.attack]

my_attack = AttackFinder("leg_attack")
print(my_attack())
