# @param {String} s
# @return {String}
def remove_stars(s)
    stack = []

    for char in s.chars
        if char != "*"
            stack.append(char)
        else
            stack.pop()
        end
    end
    return stack.join("") 
end

test_cases = [
    "leet**cod*e",
    "erase*****"
]

for test_case in test_cases
    print(remove_stars(test_case), "\n")
end