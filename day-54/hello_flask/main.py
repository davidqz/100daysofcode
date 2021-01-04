import time
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        t = time.time() - current_time
        print(f'{function.__name__} run speed: {t}s')

    return wrapper_function;


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


slow_function()
fast_function()
