from random import choice

cards = [("туз", "черви"), ("туз", "бубны"), ("туз", "черви"),("туз", "крести"), ("2", "черви"), ("2", "бубны"), ("2", "пики"), ("2", "крести"),("3", "черви"), ("3", "бубны"), ("3", "пики"), ("3", "крести"), ("4", "черви"), ("4", "бубны"), ("4", "пики"), ("4", "крести"), ("5", "черви"), ("5", "бубны"), ("5", "пики"), ("5", "крести"), ("6", "черви"), ("6", "бубны"), ("6", "пики"), ("6", "крести"), ("7", "черви"), ("7", "бубны"), ("7", "пики"), ("7", "крести"), ("8", "черви"), ("8", "бубны"), ("8", "пики"), ("8", "крести"), ("9", "черви"), ("9", "бубны"), ("9", "пики"), ("9", "крести"), ("10", "черви"), ("10", "бубны"), ("10", "пики"), ("10", "крести"), ("валет", "черви"), ("валет", "бубны"), ("валет", "пики"), ("валет", "крести"), ("дама", "черви"), ("дама", "бубны"), ("дама", "пики"), ("дама", "крести"), ("король", "черви"), ("король", "бубны"), ("король", "пики"), ("король", "крести")]

def next():
  global cards
  yield choice(cards)


N = next()
for i in N:
  print(i)