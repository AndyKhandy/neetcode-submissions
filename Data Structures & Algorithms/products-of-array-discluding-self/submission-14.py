class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for r in range(len(nums)-2, -1, -1):
            postfix[r] = postfix[r+1] * nums[r+1]
        
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]

        return output

            