# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_operations(nums, k)
    nums.sort!

    l, r = 0, nums.length - 1
    operation = 0
    while l < r
        sum = nums[l] + nums[r]
        if sum == k
            operation += 1
            l += 1
            r -= 1
        elsif sum < k
            l += 1
        else
            r -= 1
        end
    end

    return operation
end


test_cases = [
    {
        nums: [1,2,3,4],
        k: 5
    },
    {
        nums: [3,1,3,4,3],
        k: 6
    }
]

for test_case in test_cases
    print(max_operations(test_case[:nums], test_case[:k]))
end
