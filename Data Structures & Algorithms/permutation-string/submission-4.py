class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = {}

        for c in s1:
            s1Freq[c] = s1Freq.get(c,0) + 1

        l = 0 
        r = 0
        s2Freq = {}

        while r < len(s1):
            s2Freq[s2[r]] = s2Freq.get(s2[r],0) + 1
            r+=1

        #now r should equal len(s1) - 1
        
        if s2Freq == s1Freq:
            return True

        while r < len(s2):
            s2Freq[s2[l]] -= 1
            s2Freq[s2[r]] = s2Freq.get(s2[r],0) + 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l += 1
            r += 1
            
            if s2Freq == s1Freq:
                return True
        
        return False

