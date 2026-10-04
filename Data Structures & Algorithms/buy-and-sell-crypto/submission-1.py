class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0 #left = buy
        r = 1 #right = sell

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit,maxProfit)
            r+=1

        return maxProfit