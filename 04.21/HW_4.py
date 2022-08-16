import string



task = lambda x, a, b ,c: a*x**2 + b*x + c
task1 = lambda x, a, b: a*x + b

def inner(func, *args, **kwargs):
  num  = func(5, *args)

  returnType = kwargs.get("returnType")
  if returnType == "float" or returnType == None:
    return float(num)
  elif returnType == "str":
    return str(num)
    
  return num
      
  


  
function = inner(task, 211.5, 112.557, 45, returnType = "float")
function2 = inner(task, 45.14, 5.25, 14.123578, returnType = "str")
print(round(function, 2))
print(round(function2, 2))
