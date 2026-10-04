class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq,s2Freq = {}, {}

        for i in range(len(s1)):
            s1Freq[s1[i]] = s1Freq.get(s1[i], 0) + 1
            s2Freq[s2[i]] = s2Freq.get(s2[i], 0) + 1

        if s1Freq == s2Freq:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            s2Freq[s2[l]]-=1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]
            l+=1

            s2Freq[s2[r]] = s2Freq.get(s2[r],0) + 1

            if s1Freq == s2Freq:
                return True
        
        return False