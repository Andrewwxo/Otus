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
    square_list = []
    for i in args:
        square_list.append(i ** 2)
    print(square_list)

square(2, 3 ,4)


keyword = int(input("Введите степень: "))

@time_call
def square_2(*args):
    square_list = []
    for i in args:
       square_list.append(i ** keyword)
    print(square_list)
square_2(2, 3, 4)







