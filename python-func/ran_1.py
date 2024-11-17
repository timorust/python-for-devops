def randomized_speed_attack_decorator(function):
    import time
    import random

    def wrapper_func(*args, **kwargs):
        sleep_time = random.randint(0,3)
        print(f"Attack after:=> {sleep_time} seconds")
        time.sleep(sleep_time)
        return function(*args, **kwargs)
    return wrapper_func


@randomized_speed_attack_decorator
def lazy_return_random_attacks():
    import random
    from atackSchema import attacks
    while True:
        random_attack = random.choice(list(attacks.keys()))
        yield random_attack


for _ in range(5):
    print(next(lazy_return_random_attacks()))
