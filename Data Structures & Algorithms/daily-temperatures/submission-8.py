class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # values will be (index, temperature)

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                startIndex, _ = stack.pop()
                res[startIndex] = (i - startIndex)
            stack.append((i,temp))
        
        return res

