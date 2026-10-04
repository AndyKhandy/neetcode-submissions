class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w_keys = {}
        for word in strs:
            word1 = tuple(sorted(word))
            if word1 not in w_keys:
                w_keys[word1] = [word]
            else:
                w_keys[word1].append(word)
        return list(w_keys.values())
