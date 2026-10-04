class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        seenNum = set(nums)

        for num in nums:
            if (num - 1) not in seenNum:
                length = 1
                while (num + length) in seenNum:
                    length += 1
                maxLength = max(maxLength,length)
            
        return maxLength
            