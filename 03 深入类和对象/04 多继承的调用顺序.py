"""
多继承情况下：
Python 使用 C3 线性化算法（C3 Linearization） 计算 MRO。
    查找顺序按照以下规则：
        深度优先（子类 → 左侧父类 → 右侧父类）。
        避免重复（每个类仅访问一次）。
        保持继承关系的局部一致性（遵循定义时的继承顺序）。
super() 的调用：
****按照 MRO 顺序调用下一个类的方法，而不是严格的父类方法。
"""

# 深度优先案例
class A:
    def process(self):
        print("A")

class B(A):
    def process(self):
        print("B")
        super().process()

class C(A):
    def process(self):
        print("C")
        super().process()

class D(B, C):
    def process(self):
        print("D")
        super().process()

class E(C, B):
    def process(self):
        print("E")
        super().process()
print(D.mro())
D().process()