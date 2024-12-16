"""
闭包的关键特性：
    外部函数定义一个内部函数。
    内部函数可以访问外部函数的局部变量。
    外部函数返回内部函数时，内部函数仍然可以访问外部函数的局部变量，即使外部函数已经执行完毕。

"""
import functools

"""
闭包捕获的是变量的引用，而不是值
    闭包捕获的是外部函数的局部变量的引用，而不是值。因此，如果外部函数的变量在创建闭包后发生了变化，闭包中的引用也会随之改变。
"""
def outer_function():
    a = 0
    def inner_function():
        nonlocal a  # 使用 nonlocal 修改外部变量
        a += 1
        return a
    return inner_function

closure = outer_function()

print(closure())  # 输出: 1
print(closure())  # 输出: 2

def make_closures():
    l = []
    for i in range(5):
        def func(a=i):  # 默认参数使得闭包捕获当前的 i 值
            return a
        l.append(func)
    return l

closures = make_closures()

for closure in closures:
   print(closure())  # 输出: 0, 1, 2, 3, 4
# =========================================
def make_operation(operator):
    def operation(a, b):
        if operator == "add":
            return a + b
        elif operator == "subtract":
            return a - b
        elif operator == "multiply":
            return a * b
        elif operator == "divide":
            return a / b
        else:
            raise ValueError(f"Unknown operator: {operator}")
    return operation

# 创建加法和乘法函数
add = make_operation("add")
subtract = make_operation("subtract")
multiply = make_operation("multiply")
divide = make_operation("divide")

# 使用闭包计算
print(add(5, 3))         # 输出: 8
print(subtract(5, 3))    # 输出: 2
print(multiply(5, 3))    # 输出: 15
print(divide(5, 3))      # 输出: 1.666...



