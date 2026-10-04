class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l <= r:

            k = (l+r) // 2 #number of bananas per hour
            hours = 0

            for p in piles:
                hoursTaken = math.ceil(p/k)
                hours+=hoursTaken

            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k + 1

        return res


