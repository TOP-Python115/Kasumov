def count(func):
    counters = {}
    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)
    
    return wrapper
      
      

@count
def mul(a):
    print(a*3)
  
@count
def plus(b):
    print(b + 10)
 
  
@count
def min(c):
    print(c - 4)


mul(5)
min(7)
min(22)
plus(8)
plus(4)
plus(14)