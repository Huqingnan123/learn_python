def triangles():  # 列表生成器
    L = [1]
    while True:
        yield L
        L.append(0)  # 每一次都在上一行的基础上在列表末尾加个0！！！（超级巧！！！）
        # 每次第一次运算都是0+1=1作为新列表的第一个元素，第二个是L[0]+L[1],新列表有len(L)个元素
        L = [L[0]]+[L[i-1]+L[i] for i in range(1, len(L))]


n = 0
result = []
for t in triangles():
    print(t)
    result.append(t)  # 这里超级玄学！！！result有问题
    n = n+1
    if n == 10:
        break
if result == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('This is right!')
