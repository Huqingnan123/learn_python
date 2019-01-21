# numbers前面加一个*表示参数可变,可变参数
def Calculate(*numbers):
    sum = 0
    for n in numbers:  # 所有的number组成一个元组
        sum = sum+n*n
    return sum


print(Calculate(1, 2, 3, 4))
print(Calculate(5, 6, 7))
# 对于元组和列表来说，在前面加一个*相当于将其中的元素作为“可变参数“传进去
num = [1, 2, 3, 4]
print(Calculate(num[0], num[1], num[2], num[3]))
print(Calculate(*num))

# 关键字参数的用法,前面加两个**,others部分以“字典”的形式输出


def enroll(name, age, **kw):
    print('name:', name, 'age:', age, 'others:', kw)


enroll('Huqingnan', 18)
enroll('Jiangjun', 18, city='Fujian', job='Student')
dict = {'name': 'wangnengjie', 'age': 18, 'city': 'Fujian', 'job': 'coders'}
enroll(**dict)

# 通过 * 分隔来限定输入的参数名必须和后面一样,后面为命名关键字参数，一定要写清楚参数名city和job,前面的叫做位置参数，只有两个！！！


def person(name, age, *, city, job):
    print(name, age, city, job)


person('huqingnan', 18, city='Jiangxi', job='Student')
# 只能这样输入，否则就会报错！！！

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：


def persons(name, age, *args, city, job):
    print(name, age, args, city, job)


persons('jiangjun', 18, [1, 2, 3], [4, 5, 6], city='Fujian', job='Engineer')

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。
