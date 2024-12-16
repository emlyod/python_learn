"""
type 可以创建一个类
class 申明一个类
object 所有类的基类
"""
# type -> int -> obj
a = 1
b = "abc"
print(type(a)) # <class 'int'>
print(type(int)) # <class 'type'>
print(type(b)) # <class 'str'>
print(type(str)) # <class 'type'>

class Student:
    pass

stu = Student()
print(type(stu)) # <class '__main__.Student'>
print(type(Student)) # <class 'type'>
## 查看继承 (返回一个元组)
print(Student.__bases__) # (<class 'object'>,)
## type 可以创建类
## 类继承自object
## type本身也是对象 继承自object
print(type.__bases__) # (<class 'object'>,)
## object由type创建
print(type(object)) #<class 'type'>
## type自己创建了自己
print(type(type)) # <class 'type'>

## type可以创建python中的对象
## type继承了object
## object也是通过type创建的
## type是由自身创建的



