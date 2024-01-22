class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for num in asteroids:
            # print(stack)
            if len(stack) == 0:
                stack.append(num)
            
            elif stack[-1] > 0 and num < 0:

                if stack[-1] == -1 * num:
                    stack.pop()
                elif stack[-1] > -1 * num:
                    pass
                else:
                    stack.pop()
                    while len(stack) >= 1 and stack[-1] > 0 and stack[-1] < -1 * num:
                        stack.pop()
                    
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(num)
                    elif stack[-1] == -1 * num:
                        stack.pop()
            else:
                stack.append(num)

        return stack