def square(*args):
    s = []
    for i in args:
        s.append(i ** 2)
    print(s)

square(2, 3 ,4)


keyword = int(input("Введите степень: "))

def square_2(*args):
    s = []
    for i in args:
       s.append(i ** keyword)
    print(s)
square_2(2, 3, 4)
