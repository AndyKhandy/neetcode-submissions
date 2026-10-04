class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeroes = 0 
        product = 1

        for num in nums:
            if not num:
                numZeroes += 1
            else:
                product *= num
            if numZeroes == 2:
                return [0] * len(nums)

        res = [0] * len(nums)

        for i in range(len(nums)):
            if numZeroes and nums[i]:
                res[i] = 0
            elif not nums[i]:
                res[i] = product
            else:
                res[i] = int(product / nums[i])
        
        return res
        

            