"""
1.引入模块： 使用 abc 模块来定义抽象基类。
from abc import ABC, abstractmethod
2.定义抽象基类： 继承自 ABC，并在类中使用 @abstractmethod 装饰器定义抽象方法。

3.创建子类： 子类继承抽象基类，必须实现所有的抽象方法，否则子类也会被视为抽象类，不能被实例化。
4.如果子类未实现 area 或 perimeter 方法，则会抛出 TypeError，提示无法实例化抽象类。
"""

from abc import ABC, abstractmethod

# 定义一个抽象基类
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 子类必须实现所有抽象方法
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 子类实例化
rect = Rectangle(10, 20)
print(f"Area: {rect.area()}")        # Area: 200
print(f"Perimeter: {rect.perimeter()}")  # Perimeter: 60

"""
抽象基类的应用场景
1. 定义接口
抽象基类可用来定义接口，确保一组类具有统一的结构。例如，在实现多态时非常有用。
2. 限制子类行为
在大型项目中，可以通过抽象基类强制子类实现某些方法，确保代码一致性。
3. 为框架提供扩展性
许多框架通过抽象基类为开发者提供扩展接口。例如，Django 的 ORM 使用类似的抽象模式。
4. 模拟接口检查
虽然 Python 本身没有接口的概念，但可以通过抽象基类实现接口功能。
"""