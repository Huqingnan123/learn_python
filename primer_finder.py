def odd_iter():  # 从3开始的奇数序列生成器,无限序列,偶数直接不考虑
    n = 1
    while True:
        n = n+2
        yield n


def not_devisible(n):
    return lambda x: x % n != 0  # 用匿名函数lambda来表示是否整除

# 更好地理解


def not_devisible_new(n):
    def fn(x):
        return x % n != 0
    return fn  # fn闭包函数，一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。
    # 这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量，此处是n。
    # 当函数 not_devisible 的生命周期结束之后，n这个变量依然存在，因为它被闭包引用了，所以不会被回收。
    # 在 python 的函数内，可以直接引用外部变量，但不能改写外部变量。


def primer_finder():
    yield 2
    it = odd_iter()  # 构建生成器对象
    while True:
        n = next(it)
        yield n
        it = filter(not_devisible_new(n), it)  # 依次把序列中整除n的数除去，构造新序列

# 但是为什么不能将not_devisible_new(n)替换为lambda x: x % n != 0呢？
# 因为yield有“延迟”效应，就应该“调用函数传入参数n”才能用到yield将要返回的正确的n，从而正确排除一些数

# filter的第一个参数不是(not_devisible_new函数，而是_not_divisiable_new(n)这个函数调用并执行完返回的另一个"闭包"函数fn(x).
# 这个过滤器真实面目应该是filter(fn,it).
# 这样it中的元素就可以通过fn的参数传进去,而_not_divisiable(n)这种调用方式可以把n的变量值也传进去.


for n in primer_finder():
    if n <= 50:
        print(n)
    else:
        break
