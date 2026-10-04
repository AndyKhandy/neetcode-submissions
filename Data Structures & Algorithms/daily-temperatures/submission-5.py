class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stack will be a tuple of (value,index)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _,startIndex = stack.pop()
                res[startIndex] = (i - startIndex)

            stack.append((temp,i))

        return res

            