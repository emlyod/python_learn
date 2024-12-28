

# 普通函数
def add(x, y):
    return x + y

"lambda 表达式"
add_lambda = lambda x, y: x + y

print(add(3, 5))        # 输出: 8
print(add_lambda(3, 5)) # 输出: 8

# 判断一个数是奇数
is_odd = lambda x: x % 2 != 0
print(is_odd(11), is_odd(14))

"高阶函数"
# map
# 将一个函数作用于可迭代对象的每个元素，返回一个新的迭代器。
nums = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, nums)
print(list(squared))  # 输出: [1, 4, 9, 16, 25]

# filter
# 筛选出可迭代对象中符合条件的元素。
nums = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))  # 输出: [2, 4]

# reduce
# 从 functools 导入，用于累积计算。
from functools import reduce

nums = [1, 2, 3, 4, 5]
# x是初始值，y是nums中的元素，函数算出的值返回给x，第三个参数是给x赋初始值
sum_result = reduce(lambda x, y: x + y, nums, 0)
print(sum_result)  # 输出: 15

# 使用 map 将一个字符串列表转为大写
words = ['python', 'data', 'analysis']
# 输出: ['PYTHON', 'DATA', 'ANALYSIS']
upper_str = list(map(lambda x: x.upper(), words))
print(upper_str)

# 使用 filter 从列表中筛选出长度大于 3 的字符串
words = ['cat', 'elephant', 'dog', 'lion']
# 输出: ['elephant', 'lion']
bigger_str = list(filter(lambda x: len(x) > 3, words))
print(bigger_str)

# 使用 reduce 计算一个列表的乘积
nums = [1, 2, 3, 4, 5]
# 输出: 120
multiply_num = reduce(lambda x, y: x*y, nums, 1)
print(multiply_num)

# functools.partial
# 固定函数的一部分参数，创建一个新的函数。
from functools import partial
def multiply(x, y):
    return x * y
double = partial(multiply, 2)
print(double(5))  # 输出: 10

# functools.lru_cache
# 为函数添加缓存机制。
# @lru_cache(maxsize=128)
# 装饰器会缓存 fib 函数的结果，
# 最多缓存 128 个最近计算过的值。
from functools import lru_cache
@lru_cache(maxsize=128)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 输出: 55

# from functools import wraps
"""
wraps 是一个装饰器，通常用在创建自定义装饰器时。
它的作用是将原函数的元数据
（如函数名、文档字符串等）复制到装饰器函数中，
这样可以保留原函数的属性，
避免装饰器函数改变原函数的元数据。
"""
from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)
# 生成了 __le__, __gt__ 和 __ge__ 等方法
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 <= p2)  # 输出: True
print(p1 == p2) # 输出: False




