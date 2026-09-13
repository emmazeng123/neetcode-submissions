class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy
        l = 0 
        # sell
        r = 1
        maxProfit = 0


        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxProfit

