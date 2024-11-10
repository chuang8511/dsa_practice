# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_ones(nums, k)
    if nums.length == 1
        if k == 0 and nums[0] == 0
            return 0
        else
            return 1
        end
    end

    max = 0
    l, r = 0, 0
    zero_count = nums[l] == 0 ? 1 : 0

    while r < nums.length - 1
        r += 1
        if nums[r] == 0
            zero_count += 1
            if zero_count <= k
                length = r - l + 1
                max = [length, max].max
            else
                while l <= r and zero_count > k
                    if nums[l] == 0
                        zero_count -= 1
                    end
                    l += 1
                end
            end
        else
            if zero_count <= k
                length = r - l + 1
                max = [length, max].max
            elsif zero_count > k and nums[l] == 0
                zero_count -= 1
                l += 1
            end
        end
    end

    return max
end


test_cases = [
    {
        nums: [1,1,1,0,0,0,1,1,1,1,0],
        k: 2
    },
    {
        nums: [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],
        k: 3
    },
    {
        nums: [0,0,1,1,1,0,0],
        k: 0

    },
    {
        nums: [0,1,1],
        k: 0
    }
]

for test_case in test_cases
    print(longest_ones(test_case[:nums], test_case[:k]), "\n")
end