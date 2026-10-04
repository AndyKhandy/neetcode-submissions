class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sfreq = defaultdict(int)
        tfreq = defaultdict(int)

        for i in range(len(s)):
            sfreq[s[i]] = sfreq[s[i]] + 1
            tfreq[t[i]] = tfreq[t[i]] + 1
    
        return sfreq == tfreq

