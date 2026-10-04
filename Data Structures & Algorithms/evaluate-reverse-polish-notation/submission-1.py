class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token in operands:
                secondNum = int(stack.pop())
                firstNum = int(stack.pop())
                result = 0
                if token == "/":
                    result = firstNum / secondNum
                elif token == "+":
                    result = firstNum + secondNum
                elif token == "-":
                    result = firstNum - secondNum
                else:
                    result = firstNum * secondNum
                stack.append(result)
            else:
                stack.append(int(token))

        return int(stack.pop())
