class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            maxAmount = max(area,maxAmount)

            if(heights[l] > heights[r]):
                r-=1
            else:
                l+=1
        
        return maxAmount