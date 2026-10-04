class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                currPrice = prices[r] - prices[l]
                maxPrice = max(currPrice, maxPrice)
            r+=1
        return maxPrice