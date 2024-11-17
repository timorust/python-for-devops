import random
from atackSchema import attacks

def lazy_return_random_attacks():
    while True:
        random_attack = random.choice(list(attacks.keys()))
        yield random_attack

attack_generator = lazy_return_random_attacks()
print(type(attack_generator))

for _ in range(6):
    print(next(attack_generator))