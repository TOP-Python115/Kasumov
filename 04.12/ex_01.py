from random import randrange as rr
a = set([rr(1, 10) for i in range(int(input()))])
b = set([rr(1, 10) for i in range(int(input()))])
print(a, b, "\n")
print()
print(f"Не пересекающиеся элементы списков:{a ^ b}")