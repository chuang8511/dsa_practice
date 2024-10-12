class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        path_strings = path.split("/")

        for path_string in path_strings:
            if path_string in [".", ""]:
                continue
            elif path_string == "..":
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(path_string)

        return "/" + "/".join(stack)
    

test_cases = [
    "/home/",
    "/home//foo/",
    "/home/user/Documents/../Pictures",
    "/../",
    "/.../a/../b/c/../d/./"
]


solution = Solution()
for case in test_cases:
    print(solution.simplifyPath(case))