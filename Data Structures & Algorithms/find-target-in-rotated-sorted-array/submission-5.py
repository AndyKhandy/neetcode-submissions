class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        minIndex = l

        l,r = 0, len(nums) - 1

        if target >= nums[minIndex] and target <= nums[r]:
            l = minIndex
        else:
            r = minIndex - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else: 
                l = m + 1
        
        return -1