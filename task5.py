##Сложность алгоритма O(n)
def getDescentPeriods(prices):
    num = len(prices)
    dp = [1]*num
    sum = 1
    for i in range(1, num):
        if prices[i-1]-prices[i] == 1:
            dp[i] = dp[i-1]+1
        sum += dp[i]
    return sum