class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # sorted string : list

        for s in strs:
            word = tuple(sorted(s))

            res[word].append(s)
        
        return list(res.values())
