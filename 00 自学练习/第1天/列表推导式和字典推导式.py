# 列表推导式：用于快速创建列表，常见用法是从现有列表进行筛选或变换。
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
print(squares)
print(even_numbers)

# 字典推导式：用于快速创建字典。
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}

print(word_lengths)

print("1.创建一个列表，包含从1到100中所有能被3整除的数的平方。")
# 可以嵌套但不推荐，影响阅读。
divBy3List = [y for y in [x for x in range(1, 101)] if y % 3 == 0]
print(divBy3List)
print("给定一个字符串列表，生成一个字典，键为字符串，值为字符串的长度。")
