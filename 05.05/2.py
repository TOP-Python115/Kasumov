def permutation(string):
    if len(string) <1:
       yield string
    else:
        for perm in permutation(string[1:]):
            for i in range(len(set(string))):
                yield perm[:i] + string[0:1] + perm[i:]


a = permutation("abc")
for i in a:
  print(i)