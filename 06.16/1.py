# -*- coding: utf-8 -*-
import sys

class Command:
    """Команды"""
    def __init__(self, order):
        self.order = order



class BraNSh:
    def __init__(self, b):
        self.b = b

    """Словарь с командами"""
    def dict_of_commands(self):
        count = 0
        lib = {}
        for i in self.b.order:
            if i == "\n":
              break
            else:
              count += 1
              lib[f"command{count}"] = i[:-1]

        return lib

    """Вывод команд"""
    def outPut(self):
        return sys.stdout.write(str(self.dict_of_commands()))

    """Запись команд в файл"""
    def record(self):
        with open("test.txt", "w") as file:
            file.write(str(self.dict_of_commands()))




com = Command(sys.stdin.readlines())
brand = BraNSh(com)
brand.outPut()
brand.record()



