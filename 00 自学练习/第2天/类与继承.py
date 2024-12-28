"""
尽量用辅助类来维护程序状态，不要使用字典元组
不要使用包含其他字典的字典，也不要使用过长的元组
"""
from abc import ABC, abstractmethod
from collections import defaultdict
from idlelib.debugobj import ObjectTreeItem
from typing import overload, _T_co

###

"""
简单的接口接受函数，而不是类的实例
如果要用函数保持状态，那就定义新的类。并实现__call__方法
"""

# 把类变成方法
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added += 1
        return 0


current = {
    'green': 12,
    'blue': 3,
}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
# 这是一个方法
counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
print(counter.added == 2, result)

"""
以@classmethod形式的多态去通用地构造对象
使用super方法初始化父类
"""

class BaseMethod(object):
    def __init__(self, value):
        self.value = value

class TimesFiveCorrect(BaseMethod):
    def __init__(self, value):
        super().__init__(value*5)
class PlusTwoCorrect(BaseMethod):
    def __init__(self, value):
        super().__init__(value+2)

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __int__(self, value):
        super().__init__(value)

print(GoodWay.mro())
foo = GoodWay(5)
print(foo.value)
"""
编写自制容器时，可从collecions.abc模块的抽象基类中继承
"""
from collections.abc import Sequence

class MySequence(Sequence):
    @overload
    @abstractmethod
    def __getitem__(self, index: int):
        pass

    @overload
    @abstractmethod
    def __getitem__(self, index: slice):
        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def __init__(self):
        pass


