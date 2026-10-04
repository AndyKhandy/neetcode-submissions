class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        freq = {}

        l = 0
        for r, character in enumerate(s):
            freq[character] = freq.get(character,0) + 1

            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]]-=1
                l+=1
            
            maxLength = max(maxLength, (r-l+1))

        return maxLength




            