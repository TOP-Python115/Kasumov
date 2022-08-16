text = input().split()
res = {}
for i in text:
  if i in res:
    print(f"{i}_{res[i]}")
  else:
     print(i)
  res[i] = res.get(i, 0) + 1