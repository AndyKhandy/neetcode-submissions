class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = {}
        s2Freq = {}

        for i,c in enumerate(s1):
            s1Freq[c] = s1Freq.get(c,0) + 1
            s2Freq[s2[i]] = s2Freq.get(s2[i],0) + 1

        if s2Freq == s1Freq:
            return True


        l = 0 
        r = len(s1) - 1

        while r < len(s2) - 1:
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l += 1
            r += 1
            s2Freq[s2[r]] = s2Freq.get(s2[r],0) + 1
            if s2Freq == s1Freq:
                return True
        
        return False


        
        