class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxAmount = 0
        l = 0

        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                amount = prices[r] - prices[l]
                maxAmount = max(maxAmount, amount)
        
        return maxAmount
