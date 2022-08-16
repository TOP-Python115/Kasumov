## ==========  1  ========== ##

from time import perf_counter_ns, perf_counter

## class SIUnit:
    ## """Представление значений единиц СИ в удобном виде с использованием приставок единиц."""
    ## __prefixes = {0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y',
                  ## -3: 'm', -6: 'μ', -9: 'n', -12: 'p', -15: 'f', -18: 'a', -21: 'z', -24: 'y'}
    
    ## def __init__(self, number, unit, *, start_exp=0, digits=None):
        ## self.number = number
        ## self.__unit = unit
        ## self.__start_exp = start_exp
        ## for k in range(-24, 25, 3):
            ## r_number = number / 10**k
            ## if 0 < r_number < 1000:
                ## self.readable = r_number if digits is None else round(r_number, digits)
                ## self.readable_unit = f"{self.__class__.__prefixes[k+start_exp]}{unit}"
                ## break
    
    ## def __str__(self):
        ## return f"{self.readable} {self.readable_unit}"
    
    ## def target(self, target_exp):
        ## t_number = self.number * 10**(target_exp+self.__start_exp)
        ## t_unit = f"{self.__class__.__prefixes[target_exp]}{self.__unit}"
        ## return f"{t_number} {t_unit}"


def timelog_decorator(func):
    def foo(*args, **kwargs):
        print("perf_counter_ns")
        start = perf_counter_ns()
        ## все функции в Python что-то возвращают, даже если в теле функции нет инструкции 
        ##   return (в этом случае возвращается None), поэтому в декораторах общего 
        ##   назначения необходимо сохранять возвращаемое значение:
        ## func_return = func(*args, **kwargs)
        func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"Время: {end - start} ns")
        ## наносекунды пересчитываются в секунды и обратно — нет нужды повторно запускать 
        ##   счётчик и вызывать функцию func()
        ## func_time = SIUnit(end - start, 's', start_exp=-9)
        ## print(f"Время: {func_time.target(0)}")
        ## print(f"Время: {func_time!s}")
        print()
        print("perf_counter")
        s = perf_counter()
        ## func_return = func(*args, **kwargs)
        func(*args, **kwargs)
        e = perf_counter()
        print(f"Время: {e - s}")
        ## таким образом возвращается объект функции, а не её возвращаемое значение
        return func
        ## return func_return
    return foo

@timelog_decorator
def message():
    print("Hello World")

## обратите внимание, что значения времени, посчитанного с помощью perf_counter_ns() 
##   и perf_counter() сильно отличаются — это происходит потому что счётчик секунд 
##   некорректно считает очень малые (меньше микросекунды) промежутки времени, 
##   для этого нужен счётчик наносекунд
message()

print('\n')



## ==========  2  ========== ##

def count(func):
    counters = {}
    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        ## а как же файл?
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)
    return wrapper

## а как же Крестики-Нолики?
@count
def mul(a):
    print(a*3)
  
@count
def plus(b):
    print(b + 10)
  
@count
def min(c):
    print(c - 4)


mul(5)
min(7)
min(22)
plus(8)
plus(4)
plus(14)

    ## всё правильно, кроме отсутствующей записи в файл 
    ## и на действительно интересном коде не протестировано =(

print('\n')



## ==========  3  ========== ##

from time import perf_counter_ns
from sys import argv
from pathlib import Path

## script = Path(argv[0])
## journal_path = script.parents[0] / f"{script.stem}_journal.log"
path = Path("file.txt")

## что-то утомился я ваши отступы править...
## четыре пробела на один уровень отступа должно быть
## в Notepad++ меню Опции->Синтаксисы->Меню Синтаксисов->Доступные: выбрать Python 
##   правее, Настройка Табуляции->Размер табул.: установить 4, 
##   ниже, отметить ✓Заменять пробелом
## в PyCharm ещё проще, сами разберитесь, пожалуйста

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
      ## надо дополнять файл журнала, а не перезаписывать
      with open(path, "w") as file:
      ## with open(journal_path, 'a') as file:
        ## под отметкой времени имелось в виду дата и время, в которое было отправлено сообщение
        start = perf_counter_ns()
        res = func(msg, cls)
        file.write(f"{res}\n")
        end = perf_counter_ns()
        ## здесь тоже нужен конец строки
        file.write(f" Время выполнения функции {func.__name__} : {end - start} ns")
        ## почему-то мне кажется, что эта инструкция должна выполняться не из блока with
        ##   возможно, потому что её выполнение здесь не позволит корректно закрыть файл
        return res
    return _wrapper
    
  @staticmethod
  @_decorator
  ## здесь нужно было обозначить в качестве параметров экземпляр класса Person 
  ##   и строку с текстовым сообщением
  def message(msg, cls):  ## по факту, в коде ниже вы вторым аргументом 
                          ##   передаёте сюда строку, а вовсе не объект класса
    """msg - сообщение метода
       cls - возвращает объект класса"""  
    ## строки документации располагаются ПОД заголовком
    return msg, cls


pers = Person("Вусал", "vusalindahouse", "vusi444@gmail.com")
ms = TxtMsgSender()
## или можно: str(pers)
print(*ms.message("Всем привет.", pers.__str__()))

    ## пока вижу, что ещё не разобрались где какие объекты: класса, экземпляра класса и т.п.
    ## значит, надо больше практики: берите, и на ровном месте пишите самые разные классы,
    ##   навроде как я сейчас класс для единиц СИ написал
    ## не забывайте, то что я вам даю задачи в ДЗ, не значит, что вы не можете находить 
    ##   себе задачи сами =)
