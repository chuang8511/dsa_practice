# context:
# 1 + 1
# -1 + 1
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = ""
        for chr in s:
            if chr == "(":
                stack.append("(")
            elif chr == ")":
                sub_calculator = stack.pop()
                sub_result = self.operate(sub_calculator)
                # print(f"sub_result: {sub_result}")
                if stack:
                    stack[-1] += sub_result
                else:
                    result += sub_result
            else:
                if stack:
                    stack[-1] += chr
                else:
                    result += chr
        #     print(f"result: {result}")
        #     print(f"stack: {stack}")
        # print(f"op result: {self.operate(result)}")
        return int(self.operate(result))
                

    def operate(self, sub_s: str):
        print(sub_s)
        while sub_s[0] in ["(", " "]:
            sub_s = sub_s[1:]
        if len(sub_s) == 1:
            return sub_s

        l,r = 0,1
        result = 0
        while r < len(sub_s):
            
            while r < len(sub_s) and (sub_s[r].isdigit() or sub_s[r] == " "):
                r += 1
            
            if sub_s[l] in [")", "("]:
                l += 1
            elif sub_s[l] == "+":
                l += 1
                result += int(sub_s[l:r])
            elif sub_s[l] == "-":
                l += 1
                result -= int(sub_s[l:r])
            elif sub_s[l].isdigit():
                result += int(sub_s[l:r])
            l = r
            r += 1
        # print(f"result: {result}")
        return str(result)