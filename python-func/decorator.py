from functools import wraps
from time import time



def timing(fun):
    @wraps(fun)
    def wrap(*args, **kwargs):
        ts = time()
        result = fun(*args, **kwargs)
        te = time()
        print(f"fun:=> {fun.__name__}, args:=> [{args}, {kwargs}], took:=> {te - ts} seconds")
        return result
    return wrap

@timing
def some_attacks(val):
    from random_attack import attack_generator
    print(f"this was passed in:=> {val}")
    attack = attack_generator

    for _ in range(5):
        print(next(attack))
some_attacks("bar")
