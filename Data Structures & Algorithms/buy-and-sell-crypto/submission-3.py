class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l = 0
        
        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                currPrice = prices[r] - prices[l]
                maxPrice = max(maxPrice,currPrice)
        
        return maxPrice