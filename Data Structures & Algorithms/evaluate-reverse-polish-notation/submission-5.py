class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for value in tokens:
            if value == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 / num1)
                stack.append(res)
            elif value == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 + num1)
                stack.append(res)
            elif value == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 * num1)
                stack.append(res)
            elif value == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 - num1)
                stack.append(res)
            else:
                stack.append(int(value))
        return stack[-1]
