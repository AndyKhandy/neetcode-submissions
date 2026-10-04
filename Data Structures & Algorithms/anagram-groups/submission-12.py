class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1

            freqTupled = tuple(freq)
            
            if freqTupled not in res:
                res[freqTupled] = []

            res[freqTupled].append(s)
        
        return list(res.values())