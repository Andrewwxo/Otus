def number_filter(*args):
    prost = []
    chet = []
    nechet = []
    n = 0
    for i in args:
        for j in range(2, i):
            if i % j == 0:
                n += 1
        if n == 0:
            prost.append(i)
        else:
            n = 0

    print("Простые числа: ", prost)

    for i in args:
        if i%2 == 0:
            chet.append(i)

        else:
            nechet.append(i)
    print("Четные: ", chet, "Нечетные: ", nechet)


number_filter(2,3,4,5,6,7, 13, 23, 8)
