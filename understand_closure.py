def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()  # 此处count()的返回值是一个fs列表，对应赋值给f1,f2,f3
print(f1(), f2(), f3())  # 因为最后返回的时候i的值已经变成了3,所以调用函数时内部的i都成为了3

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


def counts():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # 用参数来限制变量取值，就算i最后变成了3，但是每一个i值给了一个j值，计算j*j不会受影响
    return fs

    
f11, f22, f33 = counts()
print(f11(), f22(), f33())
