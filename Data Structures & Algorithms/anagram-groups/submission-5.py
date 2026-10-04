class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            res = defaultdict(list)

            for s in strs:
                newS = tuple(sorted(s))
                res[newS].append(s)

            return list(res.values())