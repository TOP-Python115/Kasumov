from time import perf_counter_ns, perf_counter

def timelog_decorator(func):
  def foo(*args, **kwargs):
    print("perf_counter_ns")
    start = perf_counter_ns()
    func(*args, **kwargs)
    end = perf_counter_ns()
    print(f"Время: {end - start} ns")
    print()
    print("perf_counter")
    s = perf_counter()
    func(*args, **kwargs)
    e = perf_counter()
    print(f"Время: {e - s}")
    return func
  return foo

@timelog_decorator
def message():
  print("Hello World")


message()