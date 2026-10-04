class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxLength = 0

        for num in nums:
            if num - 1 not in mySet: #the start of a sequence
                length = 1
                while num + length in mySet:
                    length+=1
                maxLength = max(maxLength,length)
        return maxLength