# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    start_price = prices[0]
    profit = 0
    i = 1
    while i < prices.length
        if start_price < prices[i]
            profit += prices[i] - start_price
        end
        start_price = prices[i]
        i += 1
    end
    return profit
end


test_cases = [
    {
        prices: [7,1,5,3,6,4],
        expect: 7
    },
    {
        prices: [1,2,3,4,5],
        expect: 4
    },
    {
        prices: [7,6,4,3,1],
        expect: 0
    }
]

for test_case in test_cases
    result = max_profit(test_case[:prices])
    if result == test_case[:expect]
        print("Pass! \n")
    else
        print("Not pass, result: #{result}\n")
    end
end