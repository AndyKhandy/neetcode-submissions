class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")" : "(", "}":"{", "]" : "["}

        for c in s:
            if c in matching:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if bracket != matching[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

        