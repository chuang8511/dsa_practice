# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    l, r = 0, numbers.length - 1
    while l < r
        sum = numbers[l] + numbers[r]
        if sum == target
            return [l+1, r+1]
        elsif sum < target
            l += 1
        else
            r -= 1
        end
    end
end

test_cases = [
    {
        numbers: [2,7,11,15],
        target: 9,
        expect: [1,2],
    },
    {
        numbers: [2,3,4],
        target: 6,
        expect: [1,3],
    },
    {
        numbers: [-1,0],
        target: -1,
        expect: [1,2],
    },
]

for test_case in test_cases
    result = two_sum(test_case[:numbers], test_case[:target])
    if result == test_case[:expect]
        print("Pass!\n")
    else
        print("Not pass, result: #{result}\n")
    end
end