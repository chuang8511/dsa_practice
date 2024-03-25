class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        operator_sign = 1
        res = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c in "+-":
                res += operator_sign * num
                operator_sign = -1 if c == "-" else 1
                num = 0
            elif c == "(":
                stack.append(res)
                stack.append(operator_sign)
                res = 0
                operator_sign = 1
            elif c == ")":
                res += operator_sign * num
                previous_sign = stack.pop()
                previous_res = stack.pop()
                res *= previous_sign
                res += previous_res
                num = 0
        return res + num * operator_sign