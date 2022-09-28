import string

text = input().lower()

for i in text:
  if i in string.punctuation:
    text = text.replace(i, "")
print()


dc = {}
for c in text:
  dc[c] = 0
  dc[c] += 1

print("Словарь:")
print(dc)
