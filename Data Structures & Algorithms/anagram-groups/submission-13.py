class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sortedWord = tuple(sorted(s))
            if sortedWord not in res:
                res[sortedWord] = []
            res[sortedWord].append(s)
        
        return list(res.values())