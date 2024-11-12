# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_kth_largest(nums, k)
    nums.sort!.reverse[k-1]
end


test_cases = [
    {
        nums: [3,2,1,5,6,4], 
        k: 2,
        expect: 5
    },
    {
        nums: [3,2,3,1,2,4,5,5,6], 
        k: 4,
        expect: 4
    }
]

for test_case in test_cases
    result = find_kth_largest(test_case[:nums], test_case[:k])
    if result == test_case[:expect]
        print("Pass! \n")
    else
        print("Not pass, result: #{result}\n")
    end
end