# nums = [1,2,3,4,5]
# res =  [1,1,1,1,1]

def product_except_self(nums)

    res = [1] * nums.length

    for i in 1...nums.length
        res[i] = res[i-1] * nums[i-1]
    end

    postfix = 1
    j = nums.length - 1
    while j >= 0
        res[j] = res[j] * postfix
        postfix *= nums[j]
        j -= 1
    end

    return res
    
end