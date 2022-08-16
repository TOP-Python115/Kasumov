def palindrome(word):
  if len(word) == 1 :
    return True
  elif word == word[::-1]:
      return palindrome(word[1:-1])
  else:
      return False

word = palindrome(input())
if word == True:
  print("Правильно! Это палиндром")
else:
  print("Неправильно! Это не палиндром")