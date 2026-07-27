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

def mySqrt(x: int) -> int:
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# right是最后一个right² <= x的数
# left是第一个left² > x的数          

x = float(sys.stdin.readline())
x2 = int(sys.stdin.readline().strip())
print(my_sqrt_double(x))
print(mySqrt(x2))