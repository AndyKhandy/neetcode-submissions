class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operators:
                if token == "+":
                    b = stack.pop()
                    a = stack.pop()
                    
                    stack.append(a+b)
                if token == "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                if token == "*":
                    b = stack.pop()
                    a = stack.pop() 
                    stack.append(int(b*a))
                if token == "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return sum(stack)
        