class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCtn = 0

        for num in nums:
            if(num == 0):
                zeroCtn+=1
            else:
                totalProduct *= num
        if zeroCtn > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zeroCtn == 1:
                if c == 0:
                    res[i] = totalProduct
                else:
                    res[i] = 0
            else:
                res[i] = (totalProduct // c)

        return res
            