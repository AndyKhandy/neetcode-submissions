class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCtn = 0
        totalProduct = 1

        for num in nums:
            if num == 0:
                zeroCtn += 1
            else:
                totalProduct *= num
        if zeroCtn > 1:
            return [0] * len(nums)

        res = [1] * len(nums)

        for i, num in enumerate(nums):
            if zeroCtn == 1:
                if num == 0:
                    res[i] = totalProduct
                else:
                    res[i] = 0
            else:
                res[i] = totalProduct // num
        return res