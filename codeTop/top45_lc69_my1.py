# 平方根，二分法
import sys


def my_sqrt_double(x, eps = 1e-5):
    left, right = 0.0, x
    
    while right - left > eps:
        mid = left + (right - left) / 2
        if mid * mid <= x:
            left = mid
        else:
            right = mid
    return left


x = float(sys.stdin.readline())
print(my_sqrt_double(x))