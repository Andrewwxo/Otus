from time import time
from functools import wraps

def time_call(func):
    @wraps(func)
    def wrapper(*args):
        start = time()
        res = func(*args)
        end = time()
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")
        return res
    return wrapper

@time_call
def square(*args):
    s = []
    for i in args:
        s.append(i ** 2)
    print(s)

square(2, 3 ,4)


keyword = int(input("Введите степень: "))

@time_call
def square_2(*args):
    s = []
    for i in args:
       s.append(i ** keyword)
    print(s)
square_2(2, 3, 4)


