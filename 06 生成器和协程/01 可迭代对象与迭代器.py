"""
itertools 提供了一系列高效的迭代器工具，适合复杂数据处理场景。
常用方法
    itertools.count(start, step)：生成从 start 开始的无限序列。
    itertools.cycle(iterable)：无限循环一个可迭代对象。
    itertools.repeat(object, times)：重复一个对象。
"""


from collections.abc import Iterator
import itertools
counter = itertools.count(start=10)

for i in range(10):
    print(next(counter))

# print(len(counter)) # 报错迭代器没有len属性

print(isinstance(counter, Iterator))

a = [1, 2, 3, 4, 5]
a_iter = iter(a)  # 将可迭代对象转换为迭代器对象
print(next(a_iter))
# 生成一个循环可迭代对象
a_circle_iter = itertools.cycle(a)

for i in range(10):
    print(next(a_circle_iter))




