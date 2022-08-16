import string
a  = input("Введите первое проверочное  слово:")
b =  input("Введите второе проверочное слово:")  

for symbol in a:
  if symbol in string.punctuation:
    text = a.replace(symbol, "")
print()

for symbol in b:
  if symbol in string.punctuation:
    text = b.replace(symbol, "")
print()

if a.lower().split() == b[::-1].lower().split():
  print("Эти слова являются анаграммами")
else:
  raise ValueError("Эти слова не анаграммы")