from Task_3_Classes import Ship, Car, Plan

def main():
    ship_1 = Ship('Yacht Eclipse', 10000, 20000, 111, 13000)
    car_1 = Car('Kia Optima', 1200, 2200, 111, 4)
    plan_1 = Plan('An - 2M', 3620, 1500, 111, 4100)

    print(ship_1)
    print(car_1)
    print(plan_1)

if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(f'Пароль должен быть числом: {e.args[0]}')
