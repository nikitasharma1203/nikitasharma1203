class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current =prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < current:
                current = prices[i]
            elif prices[i] - current > profit:
                profit = prices[i] - current
        return profit

