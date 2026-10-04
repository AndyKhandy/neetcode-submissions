class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sfreq = {}
        tfreq = {}

        for i in range(len(s)):
            sfreq[s[i]] = sfreq.get(s[i],0) + 1
            tfreq[t[i]] = tfreq.get(t[i],0) + 1
    
        for key in sfreq:
            if sfreq.get(key) != tfreq.get(key):
                return False

        return True

