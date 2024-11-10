# @param {Integer[]} nums
# @return {Boolean}
def increasing_triplet(nums)
    min, mid = Float::INFINITY, Float::INFINITY

    for num in nums
        if num <= min
            min = num
        elsif num <= mid
            mid = num
        else
            return true
        end
    end

    return false
    
end