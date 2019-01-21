# 此方法属于尾递归，用初始的默认参数a=1来辅助，一直先行计算存储了上一轮相乘的积，巧！！！


def fact(n, a=1):
    if n < 0:
        pass
    elif n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return fact(n-1, n*a)  # 此处注意，只有第一次调用函数a=1，第一次之后，a的值就发生了改变！！！


print(fact(9))
