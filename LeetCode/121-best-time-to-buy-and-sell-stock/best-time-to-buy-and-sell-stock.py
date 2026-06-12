class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        n =len(prices)
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit