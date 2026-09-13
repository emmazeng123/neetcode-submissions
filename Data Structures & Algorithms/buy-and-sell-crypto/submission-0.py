class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy 
        l = 0
        #sell 
        r = 1

        maxProfit = 0 

        #sellpoint ends @ last element of array 
        while r < len(prices):
            # is stock profitable ? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                l = r
            # needs to move regardless yes/no
            r += 1       
        return maxProfit
