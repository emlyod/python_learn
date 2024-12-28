import json

it = (i * 10 for i in range(1, 21))
print(it)  # <generator object <genexpr> at 0x0000025AA4CBB370>
next(it)
print(next(it))  # 20
# 串在一起生成器执行速度很快
roots = ((x, x ** 0.5) for x in it)
print(next(roots)) # (30, 5.477225575051661)
# 表达式单独一行，是代码易读
exp = lambda x: int(x[1] ** 2)
root2 = (exp(x) for x in roots)
print(next(root2)) # 40

# 使用enumerate 取代 range
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
# 把各种迭代器包装成生成器
# i 是序列     flavor 是元素
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')

# 使用zip函数遍历两个或两个以上的迭代器
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name, max_letters)

# 尽量不要在 for 和 while 循环后面写 else 块
for i in []:
    print('不会执行')
else:
    print('For Else Block!')
i = 1
while 0 > i:
    print('不会执行')
else:
    print('For Else Block!')

# 合理利用try/except/else/finally结构中的每个代码块
UNDEFINED = object()
def divide_json(path):
    handle = open(path, 'r+')   # May raise IOError
    try:
        data = handle.read()    # May raise UnicodeDecodeError
        op = json.loads(data)   # May raise ValueError
        value = (op['numerator'] /
                 op['denominator']) # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return  UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # May raise IOError
        return value
    finally:
        handle.close()          # Allways runs
