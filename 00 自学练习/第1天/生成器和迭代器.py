

def my_generator():
    for a in range(4):
        yield a

gen = my_generator()
for i in gen:
    print(i)

print("编写一个生成器，生成斐波那契数列的前n项。")
def gen_list(n):
    m = 0
    for i in range(1, n+1):
        m += i
        yield m
gl = gen_list(10)
for i in gl:
    print(i)