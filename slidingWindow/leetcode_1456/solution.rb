# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_vowels(s, k)
    vowels = ["a", "e", "i", "o", "u"]
    if k == 0
        return 0
    end

    if k == 1
        for char in s.split("")
            if vowels.include?(char)
                return 1
            end
        end
    end

    l, r = 0, 0
    count = 1
    vowel_count = vowels.include?(s[l]) ? 1 : 0
    max = 0
    while r < s.length
        r += 1
        count += 1
        if vowels.include?(s[r])
            vowel_count += 1
        end
        if count > k 
            if vowels.include?(s[l])
                vowel_count -= 1
            end
            l += 1
            count -= 1
        end
        max = [max, vowel_count].max
    end
    return max
end

test_cases = [
    {
        s: "abciiidef",
        k: 3
    },
    {
        s: "aeiou",
        k: 2
    },
    {
        s: "leetcode",
        k: 3
    },
]

for test_case in test_cases
    print(max_vowels(test_case[:s], test_case[:k]), "\n")
end