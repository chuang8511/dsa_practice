class Solution:
    def generateParenthesis(self, n: int):
        # only add open parenthesis if openN < n
        # only add closing parenthesis if closed < open
        # Valid if openN == closedN == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        return res

solution = Solution()

testCases = [1,2,3,4,5,6]

for testCase in testCases:
    print(solution.generateParenthesis(testCase))

