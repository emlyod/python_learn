"""
1. 实例方法
定义和特点:
    绑定到实例：实例方法的第一个参数是 self，代表实例本身。
    操作实例属性：可以访问和修改实例属性，也可以通过实例访问类属性。
    通过实例调用：通常通过实例调用，但也可以通过类调用（需要显式传递实例）。
应用场景:
    需要操作实例属性或实例状态的方法。

2. 静态方法
定义和特点:
    与实例和类无关：静态方法的第一个参数没有特定意义（不需要 self 或 cls）。
    类似普通函数：但将其放在类中，表示逻辑上与该类相关。
    通过装饰器 @staticmethod 声明。
应用场景:
    逻辑上与类相关，但不需要访问实例或类的属性和方法。

3. 类方法
定义和特点
绑定到类：类方法的第一个参数是 cls，代表类本身。
操作类属性：可以访问和修改类属性，但不能直接访问实例属性。
通过装饰器 @classmethod 声明。
应用场景
需要操作或初始化与类相关的数据的方法。
"""

class BankAccount:
    interest_rate = 0.05  # 类属性

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):  # 实例方法
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    @staticmethod
    def is_positive_amount(amount):  # 静态方法
        return amount > 0

    @classmethod
    def set_interest_rate(cls, new_rate):  # 类方法
        cls.interest_rate = new_rate
        print(f"New interest rate set to {cls.interest_rate}")


# 示例
# 实例方法
account = BankAccount("Alice", 100)
account.deposit(50)  # Output: Alice deposited 50. New balance: 150

# 静态方法
print(BankAccount.is_positive_amount(50))  # Output: True
print(account.is_positive_amount(-20))    # Output: False

# 类方法
BankAccount.set_interest_rate(0.07)       # Output: New interest rate set to 0.07
