L = []
for n in range(1, 100):
    L.append(n)
r = []
for x in range(0, 100, 2):
    r.append(L[x])
print(L)
print(r)
print(L[0:10])
print(L[:10])  # “切片”快速取出前十个元素
print(L[5:10])
print(L[-10:-1])
print(L[-10:])  # 也可以倒着取出后十个

print(L[1::5])  # 从L[1]开始，每五个数取一个数

print(L[:])  # 复制列表
string = '     huqingnan is handsome!!    '
print(string[5])
if string.strip() == 'huqingnan is handsome!!':  # 调用str里面的strip函数删除首尾空格
    print('hello!')


def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s


if trim(string) == 'huqingnan is handsome!!':
    print('You are right function!')

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for s in L1:
    if isinstance(s, str):
        L2.append(s)
L2 = [s.lower() for s in L2]
print(L2)
