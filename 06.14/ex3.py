from time import perf_counter_ns
from pathlib import Path

path = Path("file.txt")

class Person:
  def __init__(self, name, login, email):
    self.name = name
    self.login = login
    self.email = email

  def __str__(self):
    return f"Меня зовут {self.name}. Вот мой логин: {self.login} и пароль: {self.email}"

class TxtMsgSender:
  
  def _decorator(func):
    def _wrapper(msg, cls):
      with open(path, "w") as file:
        start = perf_counter_ns()

        res = func(msg, cls)
        
        file.write(f"{res}\n")

        end = perf_counter_ns()

        file.write(f" Время выполнения функции {func.__name__} : {end - start} ns")

        return res
    return _wrapper
        
  """msg - сообщение метода
     cls - возвращает объект класса"""  
  @staticmethod 
  @_decorator
  def message(msg, cls):
    return msg, cls


pers = Person("Вусал", "vusalindahouse", "vusi444@gmail.com")

ms = TxtMsgSender()
print(*ms.message("Всем привет.", pers.__str__()))