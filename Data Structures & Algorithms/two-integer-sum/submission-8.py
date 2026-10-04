class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []

        myMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in myMap:
                return [myMap[diff], i]
            myMap[n] = i