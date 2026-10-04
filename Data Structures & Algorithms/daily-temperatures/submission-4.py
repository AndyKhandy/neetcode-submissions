class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # will be a stack of tuples (temperature, indexPos)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _,stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append((temp,i))
            
        return res
        

            