import sys

def fib(n: int) -> int:
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fib2(n):
    if n < 2:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)

n = int(sys.stdin.readline().strip())
print([fib(n), fib2(n)])