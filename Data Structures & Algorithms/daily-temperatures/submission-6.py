class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # will continue the tuple (index,temperature)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                startIndex,_ = stack.pop()
                result[startIndex] = (i-startIndex)

            stack.append((i,temp));
            
        return result;

            