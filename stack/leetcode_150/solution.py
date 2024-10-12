class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    c = b + a
                elif token == "-":
                    c = b - a
                elif token == "*":
                    c = b * a
                else:
                    c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(token))
        
        return stack[0]
    


test_cases = [
    ["2","1","+","3","*"],
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
]

solution = Solution()

for case in test_cases:
    print(solution.evalRPN(case))