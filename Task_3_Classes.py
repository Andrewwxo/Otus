from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):
    type_name = None

    def __init__(self, name, weight, carrying_capacity, engine_starting_password):
        self.name = name
        self.weight = weight
        self.carrying_capacity = carrying_capacity
        self.engine_starting_password = engine_starting_password

    def __str__(self):
        return f'{self.name}: Вес, кг: {self.weight}; ' \
               f'Грузоподъемность: {self.carrying_capacity}; ' \
               f'Пароль для запуска двигателя: {self.engine_starting_password}; ' \
               f'Аммортизация: {self.depreciation}' \
               f'({self.type_name})'

    @property
    @abstractmethod
    def engine_starting_password_1(self):
        return self.engine_starting_password

    @engine_starting_password_1.setter
    def engine_starting_password_1(self, val):
        try:
            engine_starting_password = int(val)
        except Exception:
            raise ValueError('Пароль должен быть числом')
        self.engine_starting_password = val

    @property
    @abstractmethod
    def depreciation(self):
        current_year = datetime.now().year
        date_of_issue = 2015  # Рассчитываю аммортизацию для транспорта 2015 года выпуска
        coefficient_depreciation = 0.05
        depreciation = (current_year - date_of_issue) * coefficient_depreciation
        return depreciation

class Ship(Vehicle):
    type_name = 'Яхты'

    def __init__(self, name, weight, carrying_capacity, engine_starting_password, displacement ):
        super().__init__(name, weight, carrying_capacity, engine_starting_password)
        self.displacement = displacement

    def engine_starting_password_1(self):
        return self

    def depreciation(self):
        return self

class Car(Vehicle):
    type_name = 'Легковые авто'

    def __init__(self, name, weight, carrying_capacity, engine_starting_password, number_of_wheels):
        super().__init__(name, weight, carrying_capacity, engine_starting_password)
        self.number_of_wheels = number_of_wheels

    def engine_starting_password_1(self):
        return self

    def depreciation(self):
        return self

class Plan(Vehicle):
    type_name = 'Самолеты'

    def __init__(self, name, weight, carrying_capacity, engine_starting_password, limit_height):
        super().__init__(name, weight, carrying_capacity, engine_starting_password)
        self.limit_height = limit_height

    def engine_starting_password_1(self):
        return self

    def depreciation(self):
        return self


