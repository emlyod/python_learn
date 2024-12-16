"""
非数学运算
    字符串表示
        __repr__
        __str__
    集合序列相关
        __len__
        __getitem__
        __setitem__
        __delitem__
        __contains__
    迭代相关
        __iter__
        __next__
    可调用
        __call__
    with上下文管理器
        __enter__
        __exit__
    数值转换
        __abs__, __bool__, __int__, __float__, __hash__, __index__
    元类相关
        __new__
        __init__
    属性相关
        __getattr__, __setattr__
        __getattribute__, __setattribute__
        __dir__
    属性描述符
        __get__, __set__, __delete__
    协程
        __await__, __aiter__, __anext__, __aenter__, __aexit__
数学运算
    一元运算符
        __eng__(-), __pos__(+), __abs__
    二元运算符
        __lt__<, __le__<=, __eq__==, __ne__!=, __gt__>, __ge__>=
    算术运算符
        __add__+, __sub__-, __mul__*, __truediv__/, __floordiv__//,
        __mod__%, __divmod__divmod(), __pow__**或者pow(), __round__round()
    反向算术运算符
        __radd__, __rsub__, __rmul__, __rturediv__, __rfloordiv__,
        __rmod__, __rdivmod__, __rpow__
    增量赋值算术运算符
        __iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__,
        __imod__, __ipow__
    位运算符
        __invert__~, __lshift__<<, __rshift__>>, __and__&, __or__|,
        __xor__^
    反向位运算符
        __rlshift__, __rrshift__, __rand__, __rxor__, __ror__
    增量赋值位运算符
        __ilshift__, __irshift__, __iand__, __ixor__, __ior__
"""

class Person:
    def __init__(self, student):
        self.student = student

    def __getitem__(self, item):
        return self.student[item]
    ## 字符串方法
    def __str__(self):
        return ",".join(self.student)
    ## 调试模式 字符串
    def __repr__(self):
        return ",".join(self.student)  # ***********
stu = Person(["柯南", "工藤", "基德"])

for i in stu:
    print(i)

## 使用print方法自动调用__str__
print(stu) # 柯南,工藤,基德

class Nums:
    def __init__(self, num):
        self.num = num
    ## 绝对值运算
    def __abs__(self):
        return abs(self.num)
mNum = Nums(-123)
print(abs(mNum)) ## 绝对值运算

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list = [1, 2, 3, 4, 5]
    ## 向量运算
    def __add__(self, other):
        re_vector = Vector(self.x+other.x, self.y+other.y)
        return re_vector
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"   # ***********
    def __len__(self):
        return  len(self.list)

v1 = Vector(10, 10)
v2 = Vector(30, 50)
print(v1+v2) # x: 40, y: 60
print(len(v2))
