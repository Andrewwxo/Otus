from Task_3_Classes import Car

class Taxi(Car):
    def __init__(self, name, weight, carrying_capacity, engine_starting_password, number_of_wheels,
                 number_of_passengers):
        super().__init__(name, weight, carrying_capacity, engine_starting_password, number_of_wheels)
        self.number_of_passengers = number_of_passengers

    def __str__(self):
            return f'{self.name}: Вес, кг: {self.weight}; ' \
                   f'Грузоподъемность: {self.carrying_capacity}; ' \
                   f'Рабочий статус: {self.vacant_taxi}'

    @property
    def vacant_taxi(number_of_passengers):
        if number_of_passengers == 0:
            return 'Vacant Taxi'
        return 'Not free Taxi'


