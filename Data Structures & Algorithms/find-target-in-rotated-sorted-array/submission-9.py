class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        
        minIndex = l # contains the index of the smallest value in the array

        l,r = 0, len(nums) - 1

        if nums[minIndex] <= target and target <= nums[r]:
            l = minIndex
        else:
            r = minIndex - 1

        # here you do the normal binary search method (you have one of the two sorte dhalfs if not sorted yet)
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1