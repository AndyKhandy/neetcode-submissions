class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1freq = {}
        s2freq = {}

        for i in range(len(s1)):
            s1freq[s1[i]] = s1freq.get(s1[i],0) + 1
            s2freq[s2[i]] = s2freq.get(s2[i],0) + 1

        if s1freq == s2freq:
            return True

        l = 0
        r = len(s1)

        while r < len(s2):
            s2freq[s2[l]] -= 1
            if s2freq[s2[l]] == 0:
                del s2freq[s2[l]]
            l+=1
            
            s2freq[s2[r]] = s2freq.get(s2[r],0) + 1
            r+=1

            if s1freq == s2freq:
                return True
        
        return False
            



