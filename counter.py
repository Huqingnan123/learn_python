# 采用列表的方法不断计数
import functools


def createcountA():
    L = [0]

    def counter():
        L[0] = L[0]+1  # L[0]会一直保存在里面
        return L[0]
    return counter


countA = createcountA()
print(countA(), countA(), countA(), countA(), countA())

# 采用生成器的方法不断生成计数


def createcountB():
    def generator():
        n = 1
        while True:
            yield n
            n = n+1
    it = generator()

    def counter():
        return next(it)
    return counter


countB = createcountB()
print(countB(), countB(), countB(), countB(), countB())

# 用全局变量的方法
n = 0


def createcountC():
    def counter():
        global n  # 引用全局变量
        n = n+1
        return n
    return counter


countC = createcountC()
print(countC(), countC(), countC(), countC(), countC())

# 匿名函数的使用
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)

int2 = functools.partial(int, base=2)
print(int2('101'))
