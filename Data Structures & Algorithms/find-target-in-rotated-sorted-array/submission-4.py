class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l

        l,r = 0, len(nums) - 1

        if target >= nums[min_index] and target <= nums[r]:
            l = min_index
        else:
            r = min_index - 1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1