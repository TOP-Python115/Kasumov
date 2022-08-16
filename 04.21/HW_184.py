def flattening(l):
    if l == list():
        return l
    if isinstance(l[0], list):
        return flattening(l[0]) + flattening(l[1:])
    return l[:1] + flattening(l[1:])


print(flattening([[45, "Hello World"], [4786, "js"], [14, "python", 25, 36]]))