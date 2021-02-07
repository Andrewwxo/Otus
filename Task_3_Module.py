from Task_3_Classes import Car
from datetime import datetime

class Taxi(Car):
    def __init__(self, name, weight, carrying_capacity, engine_starting_password, number_of_wheels,
                 number_of_passengers):
        super().__init__(name, weight, carrying_capacity, engine_starting_password, number_of_wheels)
        self.number_of_passengers = number_of_passengers

    def __str__(self):
            return f'{self.name}: Вес, кг: {self.weight}; ' \
                   f'Грузоподъемность: {self.carrying_capacity}; ' \
                   f'Рабочий статус: {self.vacant_taxi}; ' \
                   f'Аммортизация: {self.depreciation}'

    @property
    def depreciation(self):
        current_year = datetime.now().year
        year_of_production = 2015  # Рассчитываю аммортизацию для транспорта 2015 года выпуска
        coefficient_depreciation = 0.08
        depreciation = (current_year - year_of_production) * coefficient_depreciation
        return depreciation

    @property
    def vacant_taxi(number_of_passengers):
        if number_of_passengers == 0:
            return 'Vacant Taxi'
        return 'Not free Taxi'


