require 'set'
# @param {Integer[]} nums
# @return {Integer}
def longest_consecutive(nums)
    nums = Set.new(nums)
    max_length = 0
    nums.each do |num|
        if !nums.include?(num-1)
            current_num = num
            current_length = 1
            while nums.include?(current_num + 1)
                current_num += 1
                current_length += 1
                nums.delete(current_num)
            end
            max_length = [max_length, current_length].max
        end
    end
    return max_length
end


test_cases = [
    {
        nums: [100,4,200,1,3,2],
        expect: 4
    },
    {
        nums: [0,3,7,2,5,8,4,6,0,1],
        expect: 9
    },
]

for test_case in test_cases
    result = longest_consecutive(test_case[:nums])
    if result == test_case[:expect]
        print("Pass!\n")
    else
        print("Not pass, result: #{result}\n")
    end
end