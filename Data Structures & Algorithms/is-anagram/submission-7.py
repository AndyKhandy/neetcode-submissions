class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 0: Basic length check
        if len(s) != len(t):
            return False
            
        freq = {}

        # Loop 1: Populate dictionary with string s
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        # Loop 2: Decrement counts using string t
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                # If a char in t isn't in s at all, it's not an anagram
                return False
                
        # Loop 3: Verify all counts are exactly zero
        for count in freq.values():
            if count != 0:
                return False
                
        return True