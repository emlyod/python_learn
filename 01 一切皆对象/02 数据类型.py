"""
对象的三个特征:
    1.身份
    2.类型
    3.值
"""
a = None
b = None
print(id(a) == id(b)) # True

"""
None
    全局只有一个
数值类型
    int
    float
    complex(复数)
    bool
迭代类型
序列类型
    list
    bytes、bytearry、memoryview(二进制序列)
    range
    tuple
    str
    array
映射(dict)
集合
    set
    frozenset(不可变)
上下文管理类型(with) --文件管理
其他
    模块类型 --import也是类型
    class和实例
    函数类型
    方法类型
    代码类型
    object类型
    type类型
    ellipsis类型
    notimplemented类型
"""
