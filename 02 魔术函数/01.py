"""
魔术方法
    是python定义的方法
    名称不可随意修改
    是对当前类进行功能的扩展
    可以更改当前类的类型
"""


class Person:
    def __init__(self, student):
        self.student = student
    ## 魔术函数

    # 可迭代
    def __getitem__(self, index):
        # index从0开始 直到python抛出异常
        return self.student[index]

    # 序列类型
    def __len__(self):
        return len(self.student)

stu = Person(["大雨", 18, "男"])
for item in stu: ## 如果不使用__getitem__ 类是不可迭代的
    print(item)

print(len(stu)) ## 如果添加__len__ 类将没有len方法
