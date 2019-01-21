# 名字规范化，首字母大写，用切片操作（map)
from functools import reduce


def normalize(name):
    return [name[0].upper()+name[1:].lower()]


L1 = ['ADAm', 'Lisa', 'bART']
L2 = list(map(normalize, L1))
print(L2)

# 用reduce计算列表内数字的积


def multiple(x, y):
    return x*y


def prod(L):
    return reduce(multiple, L)


L = [3, 5, 7, 9]
print(prod(L))

# 运用“切片”先分割整数与小数部分，然后进行转化，，将字符串转化为浮点数


def fn(x, y):
    return x*10+y


def str2float(L):
    n = L.index('.')  # 找到小数点位置，并跳过小数点
    L1 = list(map(int, L[:n]))
    L2 = list(map(int, L[n+1:]))
    print(reduce(fn, L2)/(10**len(L2)))
    # 10**n表示10的n次方，这样又产生了小数点
    return reduce(fn, L1)+reduce(fn, L2)/(10**len(L2))


print(str2float('1234.5678'))
