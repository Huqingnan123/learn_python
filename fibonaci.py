def fib(number):  # 打印number个fibonaci数
    n, a, b = 1, 0, 1
    while n <= number:
        print(b)
        a, b = b, a+b  # 对应赋值
        n += 1
    return 'done'


number = int(input())
print(fib(number))


def fib_new(number):  # 用来定义generator生成器
    n, a, b = 1, 0, 1
    while n <= number:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'


print('\n')
for numbers in fib_new(6):  # 用生成器生成
    print(numbers)
