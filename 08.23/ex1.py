from abc import ABC, abstractmethod

# Passenger & Cargo Carriers
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items: int):
        pass

    @abstractmethod
    def carry_commercial(self, items: int):
        pass

"""Класс перевозки пассажиров"""
class Passenger(Carrier):
    """Метод перевозки военных пассажиров"""
    def carry_military(self, items: int):
        print(f"Самолет перевозит {items} военных")
    """Метод перевозки гражданских пассажиров"""
    def carry_commercial(self, items: int):
        print(f"Самолет перевозит {items} гражданских")
        
"""Класс перевозки грузов"""
class Cargo(Carrier):
    """Метод перевозки военных грузов"""
    def carry_military(self, items: int):
        print(f"Самолет перевозит {items} штук военного вооружения")
        
    """Метод перевозки гражданских грузов"""
    def carry_commercial(self, items: int):
        print(f"Самолет перевозит {items} штук бытовой техниги")





class Plane(ABC):

    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects: int):
        pass


class Military(Plane):
    """Класс военного самолета в конструкторе которого передан объект класс Сarrier и количество перевезенных объектов"""
    def __init__(self, carrier: Carrier, objects: int):
        self.carrier = carrier
        self.objects = objects

    def display_description(self):
        """Метод, который выводит на печать сведения о военных перевозках"""
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects: int):
        """Метод, добавляющий новые объекты для перевоза"""
        self.objects += new_objects

class Commercial(Plane):
    """Класс коммерческого самолета в конструкторе которого передан объект класс Сarrier и количество перевезенных объектов"""
    def __init__(self, carrier: Carrier, objects: int):
        self.carrier = carrier
        self.objects = objects

    def display_description(self):
        """Метод, который выводит на печать сведения о коммерческих перевозках"""
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects: int):
        """Метод, добавляющий новые объекты для перевоза"""
        self.objects += new_objects


cargo = Cargo()
passenger = Passenger()

mill1 = Military(cargo, 100)
mill1.display_description()
mill1.add_objects(230)
mill1.display_description()

pass1 = Commercial(cargo, 265)
pass1.display_description()

mill2 = Military(passenger, 334)
mill2.display_description()

pass2 = Commercial(passenger, 170)
pass2.display_description()