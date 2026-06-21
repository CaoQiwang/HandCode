# 买卖股票的最佳时机
# 对于每一天卖出，最优的买入日一定是之前所有天中价格最低的那天。
# 而 min(prices[0:i]) 可以通过贪心地维护得到


def max_profit(prices):
    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, prices[i])
    return max_profit


prices = [7,1,5,3,6,4]
print(max_profit(prices))