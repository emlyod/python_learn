"""
使用异常来表示特殊情况，而不要返回None
"""
import string
import time
from datetime import datetime


def divide(a, b):
    """
    :param a: 被除数
    :param b: 除数
    :return: Bool Result
    """
    try:
        return True, a / b
    except ZeroDivisionError as e:
        return False, e


isSuccess, result = divide(1, 0)
print(isSuccess, result)

"""
在闭包里使用外围作用域中的变量
"""


def sort_priority(values, groups):
    found = False

    def helper(x):
        nonlocal found
        if x in groups:
            found = True
            return False, x
        return True, x

    values.sort(key=helper)
    return found


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 4, 7}
is_found = sort_priority(numbers, group)
print(is_found, numbers)
# key接受一个筛选函数，返回一个元组
# 第一个参数：key 按照关键词对元素进行排序
# 第二个参数：元素
numbers.sort(key=lambda x: (x not in group, x))
print(numbers)


# 使用辅助类
class Sorted(object):
    def __init__(self, groups):
        self.group = groups
        self.found = False

    def __call__(self, x):
        """
        把类变成函数
        :param x: 元素
        :return: (Bool, 元素)
        """
        if x in self.group:
            self.found = True
            return False, x
        return True, x


sorter = Sorted(group)
numbers.sort(key=sorter, reverse=True)
print(sorter.found, numbers)

"""
使用生成器改写直接返回列表的函数
"""

Text = "This is a less better name !"


def my_split(text, by):
    for i in text.split(by):
        yield i if i not in string.punctuation else None


print(list(my_split(Text, ' ')))

"""
注意在参数上迭代
如果参数是列表之类的可迭代对象，尽量传入生成器
"""

def normalize_iter(get_iter):
    total = sum([v[1] for v in get_iter])  # New iterator
    for v in get_iter:  # New iterator
        # v = ('广州', 30)
        percent = 100 * v[1] / total
        yield f'{v[0]}: {percent}%'
# 将一个类变成生成器
class ReadVisits(object):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for v in self.data.strip().split('\n'):
            s = v.strip().split(' ')
            yield s[0], int(s[1])

person_data = """
    广州 30
    黑龙江 12
    成都 123
    上海 1444
    杭州 1233
"""
# 实例化类生成器
rd_iter = ReadVisits(person_data)
# 将生成器传入函数
no_iter = normalize_iter(rd_iter)
for i in no_iter:
    print(i)

"""
用数量可变的位置参数减少视觉杂讯
"""
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')
favorites = [22, 33, 2, 2]
# *favorites 变成位置参数
log('favorite number', *favorites)
# 对生成器使用*操作符，可能导致内存耗尽

"""
多使用关键字参数
用None和文档字符串来描述具有动态默认值的参数
"""

def log(message, when=None):
    """
    :param message:
    :param when:
    :return:
    """
    when = datetime.now()
    print(f'{when}: {message}')

log('Hi there!')
time.sleep(.1)
log('Hi again!')


