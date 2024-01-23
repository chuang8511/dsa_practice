class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                item = ""
                while stack[-1] != "[":
                    character = stack.pop()
                    item = character + item
                # take out [
                stack.pop()

                num = ""

                while len(stack) > 0 and stack[-1].isdigit():
                    val = stack.pop()
                    num = val + num
                stack.append(int(num) * item)

        return "".join(stack)