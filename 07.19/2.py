from abc import ABC, abstractmethod



class Kitchen(ABC):
    """Абстрактный базовый класс меню ресторана"""
    def __init__(self, menu: str):
        self.menu = menu
      
    """Абстрактный метод, который создает меню ресторана. Реализуется в производных классах """
    @abstractmethod
    def create(self):
      pass




class MexicanMenu(Kitchen):
    """Класс для воссоздания мексикансого меню ресторана"""
    def __init__(self):
        super().__init__("М")
      
        
    def create(self):
      """Метод для воссоздания мексикансого меню ресторана"""
      print("Мексиканское Меню:")
      print("Буррито")
      print("Тако")
      print("Сальса")
      print("Кесадилья")
      print("Гуакомоле")


class ChineseMenu(Kitchen):
    """Класс для воссоздания китайского меню ресторана"""
    def __init__(self):
        super().__init__("К")

    def create(self):
      """Метод для воссоздания мексикансого меню ресторана"""
      
      print("Китайское Меню:")
      print("Утка по-Пекински")
      print("Рисовые лепешки")
      print("Вонтоны")
      print("Унакимаки")
      print("Вок")


  


class MenuAbstractFactory(ABC):
    """Абстрактный метод для возвращения реализации класса Kitchen"""
    @abstractmethod
    def create_dish(self) -> Kitchen: 
      pass



class MexicanFactory(MenuAbstractFactory):
  
    """Производный класс, класса MenuAbstractFactory, для воссоздание фабрики Мексиканского меню """
  
    def create_dish(self) -> Kitchen:
        """Метод создающий фабрику мескиканского меню"""
        return MexicanMenu()


class ChineseFactory(MenuAbstractFactory):
    """Производный класс, класса MenuAbstractFactory, для 
      воссоздание фабрики Китайского меню """
  
    def create_dish(self) -> Kitchen:
        """Метод создающий фабрику китайского меню"""
        return ChineseMenu()





class Dish:
    """Класс на вход которой подается базовая  фабрика MenuAbstractFactory ."""
    def __init__(self, factory: MenuAbstractFactory):
        self.menu = factory

    def create_lunch(self):
        """Метод в котором создается экземпляр класса фабрики MenuAbstractFactory и вызывается методом create() """
        kit = self.menu.create_dish()
        kit.create()





def create_factory(kit_name: str) -> MenuAbstractFactory :
    if kit_name == "1":
        return MexicanFactory()
    elif kit_name == "2":
        return ChineseFactory()

    

if __name__ == '__main__':
    kitchen = input("Выберите меню:\nМексиканское - 1\nКитайское - 2\n")
    fac = create_factory(kitchen)
    dish = Dish(fac)
    dish.create_lunch()
