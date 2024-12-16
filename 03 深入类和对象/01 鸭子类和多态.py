"""
多态
    继承: 多态一定是发生在子类和父类之间的
    重写: 子类重写父类中的方法
"""
class Animal:
    def say(self):
        print("I am Animal")

class Cat(Animal): # 继承Animal
    def say(self):
        print("I am cat")

class Dog(Animal): # 继承Animal
    def say(self):
        print("I am dog")

class Duck(Animal): # 继承Animal
    def say(self):
        print("I am duck")
dog = Dog()
dog.say()

"""
鸭子类型
    一种动物长得像鸭子 叫起来也像鸭子 那么这个动物就是一个鸭子
****多个类中实现了同一个方法(当前的方法名称一样)
"""
animal = Cat
animal().say() # I am cat

animal = Dog
animal().say() # I am dog

aniList = [Cat, Dog, Duck]
for instance in aniList:
    instance().say()

## 鸭子类型案例
a = [1, 2]
b = [3, 4]

a.extend(b)
print(a) # [1, 2, 3, 4]

c = set()
c.add(5)
c.add(6)

a.extend(c)
print(a) # [1, 2, 3, 4, 5, 6]
"""
extend 只要是迭代对象 就可以进行追加
list
set
    都是可迭代对象
    __iter__
    __next__
共为可迭代类
"""
