num = input("Введите не менее четырех целых чисел: ").split()
while len(num) < 4:
  print("Ошибка")
  num = input("Введите не менее четырех целых чисел: ").split()
  
newList = [int(i) for i in sorted(num)]
print(*newList) 