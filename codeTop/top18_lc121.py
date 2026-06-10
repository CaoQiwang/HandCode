# 买卖股票最佳时机
import sys


def maxProfix(prices):
    max_profix = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        profix = prices[i] - min_price
        min_price = min(min_price, prices[i])
        max_profix = max(max_profix, profix)
    
    return max_profix


nums = list(map(int, sys.stdin.readline().strip().split()))
print(maxProfix(nums))