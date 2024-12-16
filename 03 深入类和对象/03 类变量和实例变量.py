"""
1.类变量
类变量是绑定在类上的属性，所有实例共享同一个值。通常用于存储与类相关的公共数据。

特点:
    声明位置：直接在类体中（但不在方法中）。
    作用范围：所有实例共享，类本身也可以访问。
    修改方式：通过类名或实例修改，但通过实例修改会创建一个实例变量，而不影响原来的类变量。
"""

class Example:
    class_var = "I am a class variable"  # 类变量

# 通过类名访问
print(Example.class_var)  # Output: I am a class variable

# 实例共享类变量
obj1 = Example()
obj2 = Example()
print(obj1.class_var)  # Output: I am a class variable
print(obj2.class_var)  # Output: I am a class variable

# 修改类变量
Example.class_var = "Class variable modified"
print(obj1.class_var)  # Output: Class variable modified
print(obj2.class_var)  # Output: Class variable modified

"""
2.实例变量
定义:
实例变量是绑定到某个实例对象的属性，不能被其他实例直接共享。
特点:
    声明位置：通常在 __init__ 方法中，使用 self 引用。
    作用范围：仅在当前实例中有效，其他实例有自己独立的实例变量。
    修改方式：只能通过实例修改，不影响其他实例。
"""

"""
类变量覆盖问题： 如果通过实例修改类变量，会创建同名的实例变量，而不会真正修改类变量。
避免混淆： 如果变量名相同且用实例访问，优先访问实例变量。

"""

class BankAccount:
    # 私有类变量，不允许外部直接访问或修改
    __interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def apply_interest(self):
        """应用利息到账户余额"""
        self.balance += self.balance * BankAccount.__interest_rate

    @classmethod
    def get_interest_rate(cls):
        """获取当前利率"""
        return cls.__interest_rate

    @classmethod
    def set_interest_rate(cls, new_rate):
        """设置新的利率（带验证）"""
        if new_rate < 0 or new_rate > 1:
            raise ValueError("Interest rate must be between 0 and 1.")
        cls.__interest_rate = new_rate

# 示例
# 创建账户
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)

# 查看默认利率
print(BankAccount.get_interest_rate())  # Output: 0.05

# 应用利息
account1.apply_interest()
account2.apply_interest()
print(account1.balance)  # Output: 1050.0
print(account2.balance)  # Output: 2100.0
# 修改利率
BankAccount.set_interest_rate(0.1)
#account1.set_interest_rate(1.0)
# 查看修改后的利率
print(BankAccount.get_interest_rate())  # Output: 0.1
# 应用新的利率
account1.apply_interest()
account2.apply_interest()
print(account1.balance)  # Output: 1155.0
print(account2.balance)  # Output: 2310.0
