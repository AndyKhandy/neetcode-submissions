class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        l, r = 0, len(heights) - 1

        while l < r:
            distance = r - l
            minHeight = min(heights[l], heights[r])
            currentArea = distance * minHeight
            maxAmount = max(currentArea, maxAmount)

            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1

        return maxAmount
