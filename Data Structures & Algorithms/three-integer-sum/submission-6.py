class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        for i, n in enumerate(nums):
            if n > 0:
                continue
            if i > 0 and n == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = n + nums[j] + nums[k]
                if total == 0:
                    res.append([n, nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while k > j and nums[k] == nums[k+1]:
                        k-=1
                elif total > 0:
                    k-=1
                else:
                    j+=1
        return res