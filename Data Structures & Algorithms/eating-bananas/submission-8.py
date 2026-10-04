class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for example 1 it would 1, 4 
        # since piles.lenth <= h the max amount of bananas you could eat per hour and make it would be the mos tbanas in a pile
        l,r =  1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            totalHours = 0

            for pile in piles:
                hoursTaken = math.ceil(pile/k)
                totalHours += hoursTaken

            if totalHours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        
        return res
