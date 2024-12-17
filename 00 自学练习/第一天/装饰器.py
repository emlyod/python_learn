import functools
import sys
import time

sys.set_int_max_str_digits(10000)
def calculator(unit, s):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            exec_time = end_time-start_time
            # 确定时间单位
            if unit == "ms":
                exec_time *= 1000
            if isinstance(result, int):
                if s == "hex":
                    result = hex(result).split("x")[1]
                elif s == "oct":
                    result = oct(result).split("o")[1]
            else:
                print("Result is not an integer, cannot convert.")
            print(f"Execution time: {exec_time:.2f} {unit}")
            return f'Result in {s}: {result}'
        return wrapper
    return decorator

@calculator("ms", "hex")
def calc_mod(num, mod):
    return num**mod

print(calc_mod(999, 3000))


