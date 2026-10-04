class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high; use two pointers if the value at the l pointer is > value at r pointer 
        # make the l pointer = r pointer

        maxPrice = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                currProfit = prices[r] - prices[l]
                maxPrice = max(maxPrice,currProfit)
        
        return maxPrice