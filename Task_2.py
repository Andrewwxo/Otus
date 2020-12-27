import time
from functools import wraps


def time_call(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        time_taken = time.time() - start_time
        print(f"time taken: {time_taken:.13f}")
        return res

    return wrapper

@time_call
def prime_number(numbers):
    prime_list = []
    n = 0
    for i in numbers:
        for j in range(2, i):
            if i % j == 0:
                n += 1
        if n == 0:
            prime_list.append(i)
        else:
            n = 0

    print("Prime numbers: ", prime_list)


@time_call
def chet_nechet(numbers):
    chet = []
    nechet = []
    for i in numbers:
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    print("Even numbers: ", chet, "Odd numbers: ", nechet)


if __name__ == "__main__":
    numbers = 1, 2, 3, 4, 7, 15, 17, 22
    prime_number(numbers)
    chet_nechet(numbers)
