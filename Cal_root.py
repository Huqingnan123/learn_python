import math


def quadratic(a, b, c):
    x1 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    if x1 == x2:
        return x1
    else:
        return x1, x2


r1 = quadratic(3, 4, 1)
print(r1)
r2 = quadratic(2, 2, -1)
print(r2)
