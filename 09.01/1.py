from random import choice as ch
from abc import ABC, abstractmethod


class Request(ABC):
    @abstractmethod
    def next_request(self, request: "Server"):
      """Метод, который передает выполнение команды следующему в цепочке ответсвенности"""
      pass
    
    @abstractmethod
    def execute(self, order: int):
      """Метод, принимающий команду на исполнение """
      pass


class Server(Request):
    """Класс, реализующий интерфейс абстрактного класса Request"""
    def __init__(self):
        self.__next_request = None

    def next_request(self, request: Request):
      """Метод, реализующий интервейс абстрактного метода next_request"""
      self.__next_request = request
      return request

    def execute(self, order: int):
        """Метод, котору передается команда на исполнение, если она есть среди списка команд"""
        if self.__next_request is not None:
            return self.__next_request.execute(order)
        return "Отправленного вами запроса не существует"


class OK(Server):
    """Класс, реализующий  запрос 200. В случае передачи другого запроса, делегируем его следующему в цепочке. """
  
    def execute(self, order: int):
        if order == 200:
            return "Code 200 - OK"
        else:
            return  super().execute(order)


class Forbidden(Server):
    """Класс, реализующий  запрос 403. В случае передачи другого запроса, делегируем его следующему в цепочке. """
  
    def execute(self, order: int):
        if order == 403:
            return "Code 403 - Forbidden"
        else:
            return  super().execute(order)

class NotFound(Server):
    """Класс, реализующий  запрос 404. В случае передачи другого запроса, делегируем его следующему в цепочке. """
  
    def execute(self, order: int):
        if order == 404:
            return "Code 404 - Not found"
        else:
            return super().execute(order)

class InternalServerError(Server):
    """Класс, реализующий  запрос 500. В случае передачи другого запроса, делегируем его следующему в цепочке. """
  
    def execute(self, order: int):
        if order == 500:
            return "Code 500 - Internal Server Error"
        else:
            return super().execute(order)


ok = OK()
forbidden = Forbidden()
not_found = NotFound()
internal = InternalServerError()

#Список запросов. А также пустой запрос для проверки
list_of_request = [200, 403, 404, 500, ""]

# Цепочка ответсвенности при помощи вызова метода next_request()
ok.next_request(forbidden).next_request(not_found).next_request(internal)

#Выполнение метода execute() в который передается случайный запрос из списка list_of_request
req = ok.execute(ch(list_of_request))
print(req)