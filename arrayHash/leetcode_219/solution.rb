# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
    # { 1: [0, 1, 2] }
    hash = {}
    nums.each_with_index do |num, i|
        # print(hash, "\n")
        # print(i, "\n")
        # print(num)
        if hash[num]
            diff = i - hash[num][-1]
            if diff <= k
                return true
            end
            hash[num].append(i)
        else
            hash[num] = [i]
        end
    end
    return false
end


test_cases = [
    {
        nums: [1,2,3,1],
        k: 3,
        expect: true
    },
    {
        nums: [1,0,1,1],
        k: 1,
        expect: true
    },
    {
        nums: [1,2,3,1,2,3],
        k: 2,
        expect: false
    }
]

for test_case in test_cases
    result = contains_nearby_duplicate(test_case[:nums], test_case[:k])
    if result == test_case[:expect]
        print("Pass!\n")
    else
        print("Not pass, result: #{result}\n")
    end
end