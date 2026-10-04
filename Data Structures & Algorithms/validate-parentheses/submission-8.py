class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for token in s:
            if token in closeToOpen:
                if stack and closeToOpen[token] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(token)

        return len(stack) == 0