# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    l, r = 0, 1
    max_profit = 0
    while r < prices.length
        profit = prices[r] - prices[l]
        max_profit = [profit, max_profit].max
        if prices[l] > prices[r]
            l = r
        end
        r += 1
    end
    return max_profit
end


test_cases = [
    {
        prices: [7,1,5,3,6,4],
        result: 5
    },
    {
        prices: [7,6,4,3,1],
        result: 0
    },
]

for test_case in test_cases
    result = max_profit(test_case[:prices])
    if result == test_case[:result]
        print("Pass!\n")
    else
        print("Not pass, result #{result}\n")
    end
end