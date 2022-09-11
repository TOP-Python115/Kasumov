class Alphabet:
  """self.a первая буква в list_of_letters() и self.b - последняя буква для list_of_letters """
  def __init__(self, lang: str,
                     a: str, 
                     b: str) -> None:
    self.lang = lang
    self.a = a
    self.b = b
  
  """Возвращаем язык"""
  def which_lang(self):
    return self.lang
    
  """Список букв в алфавите """  
  def list_of_letters(self):
    list_ = []
    for i in range(ord(self.a),ord(self.b)+1):
     list_+=chr(i)
    return list_ 
    




class English(Alphabet):
  def __init__(self, lang:str,
                     a: str, 
                     b: str, 
                     item: str) -> None:
    super().__init__(lang , a, b)
    self.item = item

    
  """Количество букв"""  
  def quantity(self):
    count = 0
    for i in self.list_of_letters():
      count+=1
    return count
    
  """Относится ли буква к текущему алфавиту"""
  def substring(self):
    if self.item in self.list_of_letters():
      return "Correct"
    else:
      return "There is no such letter in english alphabet"

  """Текст на данном языке""" 
  def __str__(self):
    text = f"Random text in English"
    return text

class Russian(Alphabet):
  def __init__(self, lang:str, 
                     a:str,
                     b:str, 
                     item:str) -> None:
    super().__init__(lang, a, b)
    self.item = item

    
  """Количество букв"""  
  def quantity(self):
    count = 0
    for i in self.list_of_letters():
      count+=1
    return count + 1

  """Относится ли буква к текущему алфавиту"""
  def substring(self):
    if self.item in self.list_of_letters():
      return "Правильно"
    else:
      return "В русском алфавите нет такой буквы"
    
  """Текст на данном языке""" 
  def __str__(self):
    text = f"Рандомный текст на русском языке"
    return text
    

	 


eng = English("english", "a", "z", "р")
print(f"List of letters in the english alphabet: {eng.list_of_letters()}")
print(f"The number of letters in the English alphabet: {eng.quantity()}")
print(eng.substring())
print(eng.__str__())

print()
print()

ru = Russian("русский",  "а", "я", "р")
print(f"Список букв в русском алфавите: {ru.list_of_letters()}")
print(f"Количество букв в русском алфавите: {ru.quantity()}")
print(ru.substring())
print(ru.__str__())
