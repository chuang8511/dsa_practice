# @param {String} word1
# @param {String} word2
# @return {Boolean}


def close_strings(word1, word2)
    return false if word1.length != word2.length

    hash_1 = {}
    for w in word1.split("")
        if hash_1[w]
            hash_1[w] += 1
        else
            hash_1[w] = 0
        end
    end

    hash_2 = {}
    for w in word2.split("")
        if hash_2[w]
            hash_2[w] += 1
        else
            hash_2[w] = 0
        end
    end
    hash_1_keys = hash_1.keys().sort!
    hash_1_values = hash_1.values().sort!
    hash_2_keys = hash_2.keys().sort!
    hash_2_values = hash_2.values().sort!

    return hash_1_keys == hash_2_keys && hash_1_values == hash_2_values
end

test_cases = [
    {
        word1: "abc",
        word2: "bca",
    },
    {
        word1: "a",
        word2: "aa",
    },
    {
        word1: "cabbba",
        word2: "abbccc",
    }
]

for test_case in test_cases
    print(close_strings(test_case[:word1], test_case[:word2]), "\n")
end