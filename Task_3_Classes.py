class Vehicle:
    type_name = None

    def __init__(self, name, weight, carrying_capacity):
        self.name = name
        self.weight = weight
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        return f'{self.name} ({self.type_name})'

    def sound(self):
        print('sound on')

class Ship(Vehicle):
    type_name = 'Яхты'

    def __init__(self, name, weight, carrying_capacity, displacement):
        super().__init__(name, weight, carrying_capacity)
        self.displacement = displacement

class Car(Vehicle):
    type_name = 'Легковые авто'

    def __init__(self, name, weight, carrying_capacity, number_of_wheels):
        super().__init__(name, weight, carrying_capacity)
        self.number_of_wheels = number_of_wheels

class Plan(Vehicle):
    type_name = 'Самолеты'

    def __init__(self, name, weight, carrying_capacity, limit_height):
        super().__init__(name, weight, carrying_capacity)
        self.limit_height = limit_height

ship_1 = Ship('Yacht Eclipse', 10000, 20000, 13000 )
car_1 = Car('Kia Optima', 1200, 2200, 4)
plan_1 = Plan('An - 2M', 3620, 1500, 4100)

print(ship_1)
print(car_1)
print(plan_1)

print(ship_1.weight)