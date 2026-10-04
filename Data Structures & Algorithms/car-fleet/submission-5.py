class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,q) for p,q in zip(position,speed)]
        stack = []

        for p,q in sorted(pairs)[::-1]:
            stack.append((target-p) / q)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
            
