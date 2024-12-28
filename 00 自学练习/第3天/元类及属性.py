"""
用纯属性取代get和set方法
访问某个对象属性是，需要表现出特殊的的行为，那就用@property来定义这种行为
@property方法需要执行的迅速一些，缓慢或复杂的工作应该放在普通的方法里面
"""
import functools
import json
import time
from weakref import WeakKeyDictionary


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms  # 电阻
        self.voltage = 0  # 电压
        self.current = 0  # 电流


#
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print(f'before: {r2.current} amps')
r2.voltage = 10
print(f'after: {r2.current} amps')

"""
@property 可以为现有的实例属性添加新的功能
可以用@property来逐步完善数据模型
如果@property属性用的太频繁，那就考虑彻底的重构该类并修改相关调用代码
"""

"""
如果想复用@property方法及其验证机制，那可以自己定义 描述符类
WeakKeyDictionary可以保证描述符类不会泄露内存
通过描述符协议类实现属性的获取和设置操作时，不要纠结于__getattribute__的方法具体的运作细节

"""


class Grade(object):
    def __init__(self):
        # 可回收的字典
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100.')
        self._values[instance] = value


class Exam(object):
    # class attributes
    # 描述符协议
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.math_grade = 80
exam.science_grade = 70
# exam.writing_grade = -1 # 报错
print(exam.math_grade)
print(exam.writing_grade)

"""
通过__getattr__和__setattr__可用惰性的方式来加载保存对象属性
__getattr__和__getattribute__区别: 前者会在访问的属性缺失时触发，后者会在每次访问属性的时候触发
如果要在__getattribute__和__setattr__方法中访问实例属性，应该直接用super()object的同名方法来做，以避免无限递归。
"""


def exec_something(name: str):
    """
    装饰器: 打印类容日志
    :param name:
    :return:
    """

    def decorator(func):
        functools.partial(func)

        def wrapper(*args, **kwargs):
            if name == "create":
                print(f'Tile: {name}')
                value = func(*args, **kwargs)
                print(f'Log: Attr {args[1]} has been created.')
            elif name == "time":
                print(f'Tile: {name}')
                value = func(*args, **kwargs)
                print(f'Log: Current time is {time.ctime()}')
            else:
                raise f'exec_something hasn\'t string {name}.'
            return value

        return wrapper

    return decorator


class AddMyAttr(object):
    def __init__(self):
        self.count = 1

    @exec_something("create")
    def __getattr__(self, name):
        print(f'Call __getattr__({name})')
        # 设置属性超过3个则报错
        if len(self.__dict__) > 3:
            raise "attrs count are above five."
        else:
            try:
                return super().__getattribute__(name)
            except AttributeError:
                value = self.count
                setattr(self, name, value)  # 设置属性和值
                self.count += 1
                return value


my_attr = AddMyAttr()
print(my_attr.__dict__)  # 打印属性字典
print(my_attr.first)
print(my_attr.second)
print(hasattr(my_attr, 'third'))  # 第一次调用__getattr__
print(getattr(my_attr, 'third'))  # 第二次不会调用了
print(hasattr(my_attr, 'third'))  # 第二次不会调用了
# print(my_attr.forth)  # 设置属性超过3个报错
print(my_attr.__dict__)  # 打印属性字典

print('=======================================')


class AddMyAttribute(object):
    def __init__(self):
        self.count = 1

    # 每次调用获取属性时都会调用这个函数，不管属性存不存在。
    def __getattribute__(self, item):
        print(f'Called __getattribute__({item})')
        try:
            value = super().__getattribute__(item)
            return value
        except AttributeError as e:
            setattr(self, item, False)
            return False

    # setattr 挂钩
    def __setattr__(self, key, value):
        print(f'Log: Called __setattr__{key, value}')
        super().__setattr__(key, value)


# 实例化时 Log: Called __setattr__('count', 1)
my_attribute = AddMyAttribute()
# 创建属性时 Log: Called __setattr__('data', False)
print(my_attribute.data)
# 每次调用hasattr()或getattr()都会调用__getattribute__
print(hasattr(my_attribute, 'count'))
print(hasattr(my_attribute, 'data'))

print('=============================================')
"""
通过元类，可以在生成子对象之前先验证子类的定义是否合乎规范
python系统把子类的整个class语句体处理完毕之后，就会调用其元类的__new__方法
"""


class Meta(type):
    def __new__(cls, name, bases, class_dict):
        print((cls, name, bases, class_dict))
        return type.__new__(cls, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 3

    def foo(self):
        pass


class ValidatePolygon(type):
    def __new__(cls, name, bases, class_dict):
        # 不验证Polygon 抽象基类
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides.')
        return type.__new__(cls, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # Specifed by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


# 报错 sides 必须大于3
# class Line(Polygon):
#     sides = 1

print('=====================================')
"""
使用元类来注册子类
在模块化的python程序，类的注册是很有用的模式
每次从基类继承子类时，基类的元类都可以自动运行注册代码
通过元类来实现类的注册，可以确保所有子类都不会遗漏，从而避免后续错误
"""

class RegisterClass(object):
    registry = {}
    @classmethod
    def register_class(cls, target_class):
        cls.registry[target_class.__name__] = target_class


class RegisterMate(type):
    def __new__(cls, name, bases, class_dict):
        cls = type.__new__(cls, name, bases, class_dict)
        if bases != (object, ):  # 不将基类注册
            RegisterClass.register_class(cls)
            return cls
        return cls


class Serializable(object, metaclass=RegisterMate):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'class': self.__class__.__name__,
                           'args': self.args, })

    def deserialize(self, data: str):
        params = json.loads(data)
        name = params['class']
        target_class = RegisterClass.registry[name]
        return target_class(*params['args'])


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'
# 创建类，将类注册放在注册器中
class Point3D(Serializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point3D({self.x}, {self.y}, {self.z})'

point2d = Point2D(5, 4)
print(f'Object: {point2d}')
d = point2d.serialize()
print(d)
s = point2d.deserialize(d)
print(s)
point3d = Point3D(2, 4, 6)
print(point3d)
d1 = point3d.serialize()
print(d1)
s1 = point3d.deserialize(d1)
print(s1)
print(RegisterClass.registry)

print('=======================================')
"""
借助元类，可以定义某个类完全定义好之前，率先修改该类的属性
描述符和元类结合起来，对某些行为做出修饰，或在程序运行时探查相关信息
就可以在不使用weakref模块的前提下避免内存泄露
"""
class Field(object):
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class ChangeAttrMate(type):
    def __new__(cls, name, bases, class_dict: dict):
        for k, v in class_dict.items():
            if isinstance(v, Field):
                v.name = k
                v.internal_name = '_' + k
        cls = type.__new__(cls, name, bases, class_dict)
        return cls

class DatabaseRow(object, metaclass=ChangeAttrMate):
    pass

class Customer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

foo = Customer()
print(f'Before: {repr(foo.first_name)} {foo.__dict__}')
foo.first_name = 'Euler'
foo.last_name = 'Flee'
print(f'after: {repr(foo.first_name)} {foo.__dict__}')
