num = input("Введите целые числа: ").split()
while len(num) < 4:
  print("Ошибка. Вы должны ввести не менее четырех чисел!")
  num = input("Введите целые числа: ").split()
  
list = []
list.extend(num)
print(list)

newList =  [int(i) for i in list if i != max(list) and i != min(list)]
print(*newList)
