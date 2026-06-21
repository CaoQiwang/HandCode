# 买卖股票的最佳时机2
# 只看从第二天开始每日的收益，如果为正就加进去

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        profix = prices[i] - prices[i-1]
        if profix > 0:
            max_profit += profix
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))