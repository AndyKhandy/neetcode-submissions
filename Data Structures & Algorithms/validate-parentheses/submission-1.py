class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")" : "(", "}" : "{", "]" : "["}

        for bracket in s:
            if bracket in matching:
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if matching[bracket] != openBracket:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0
        