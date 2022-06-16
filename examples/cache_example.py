from time import sleep, time
from functools import lru_cache

CACHE = {}

def foo(sleep_time, power):
    global CACHE

    key_cache = f'foo::{sleep_time}::{power}'

    if key_cache not in CACHE:
        sleep(sleep_time)
        result = sleep_time ** power
        CACHE[key_cache] = result
        return result
    else:
        return CACHE[key_cache]


def sub(x, y):
    global CACHE

    key_cache = f'sub::{x}::{y}'

    if key_cache not in CACHE:
        result = x - y
        CACHE[key_cache] = result
        return result
    else:
        return CACHE[key_cache]

start = time()
# print(foo(2, 2))  # 4
# print(sub(2, 2))  # 0
# print(CACHE)
print(f'Took: {time() - start} seconds.')


'''
f() - 15 min

1. 45  f(45) - 250 
2. 50  f(50) - 275
3. 45  f(45) - 250
4. 45  f(45) - 250
'''

@lru_cache
def foo_real(sleep_time, power):
    sleep(sleep_time)
    result = sleep_time ** power
    return result

start = time()
print(foo_real(2, 3))
print(foo_real(2, 3))
print(foo_real(2, 3))
print(foo_real(2, 3))
print(foo_real(2, 5))
print(foo_real(2, 5))
print(foo_real(2, 5))
print(f'Took: {time() - start} seconds.')


@custom_cache  # velociped kak lru_cache
def foo_with_deco(sleep_time, power):
    sleep(sleep_time)
    result = sleep_time ** power
    return result
