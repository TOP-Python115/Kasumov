def mutual_div(a, b):
    if (b == 0):
        return a
    else:
        return mutual_div(b, a % b)
a = int(input("a = "))
b = int(input("b = "))


mutual_div = mutual_div(a, b)
print(mutual_div)
