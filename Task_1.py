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
def square(numbers):
    square_list = []
    for i in numbers:
        square_list.append(i ** 2)
    print(square_list)

@time_call
def square_2(numbers):
    square_list = []
    for i in numbers:
       square_list.append(i ** keyword)
    print(square_list)


if __name__ == '__main__':
    numbers = 2, 3, 4
    square(numbers)
    keyword = int(input("Введите степень: "))
    square_2(numbers)



