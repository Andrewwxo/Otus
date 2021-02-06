from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass


class VehicleMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_class = super().__new__(mcs, name, bases, attrs)
        if 'year_of_production' not in attrs:
            new_class.year_of_production = None
        return new_class

class Vehicle(metaclass=VehicleMeta):
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



class Ship(Vehicle):
    type_name = 'Яхты'

    def __init__(self, name, weight, carrying_capacity, engine_starting_password, displacement ):
        super().__init__(name, weight, carrying_capacity, engine_starting_password)
        self.displacement = displacement

    def engine_starting_password_1(self):
        return self


class Car(Vehicle):
    type_name = 'Легковые авто'

    def __init__(self, name, weight, carrying_capacity, engine_starting_password, number_of_wheels):
        super().__init__(name, weight, carrying_capacity, engine_starting_password)
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        return f'{self.name}: Вес, кг: {self.weight}; ' \
               f'Грузоподъемность: {self.carrying_capacity}; ' \
               f'Пароль для запуска двигателя: {self.engine_starting_password}; ' \
               f'Аммортизация: {self.depreciation}' \
               f'({self.type_name})'

    def engine_starting_password_1(self):
        return self

    @abstractmethod
    def depreciation(self):
        current_year = datetime.now().year
        year_of_production = 2015  # Рассчитываю аммортизацию для транспорта 2015 года выпуска
        coefficient_depreciation = 0.05
        depreciation = (current_year - year_of_production) * coefficient_depreciation
        return depreciation


@dataclass
class Plan(Vehicle):
    type_name = 'Самолеты'

    name: str
    weight: int
    carrying_capacity: int
    engine_starting_password: int
    limit_height: int


    def engine_starting_password_1(self):
        return self





