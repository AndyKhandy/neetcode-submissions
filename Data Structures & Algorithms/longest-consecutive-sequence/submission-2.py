class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        mySet = set(nums)

        for num in nums:
            if (num - 1) not in mySet: #beginning of a sequence 
                length = 1;
                while num + length in mySet:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength
            