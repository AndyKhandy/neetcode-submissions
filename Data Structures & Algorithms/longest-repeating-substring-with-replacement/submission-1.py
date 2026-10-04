class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {}
        maxLength = 0
        l = 0

        for r in range(len(s)):
            myMap[s[r]] = myMap.get(s[r],0) + 1

            while r - l + 1 - max(myMap.values()) > k:
                myMap[s[l]] -= 1
                l += 1

            length = r - l + 1
            maxLength = max(length,maxLength)
        
        return maxLength


            

            