# @param {String} pattern
# @param {String} s
# @return {Boolean}
def word_pattern(pattern, s)
    words = s.split(" ")
    return false if words.length != pattern.length
    hash = {}
    word_hash = {}
    
    for i in 0..words.length-1
        char = pattern[i]
        # print(char, "\n")
        # print(words[i], "\n")
        if hash[char]
            return false if hash[char] != words[i]
        else
            hash[char] = words[i]
            if word_hash[words[i]].nil?
                word_hash[words[i]] = true
            else
                return false
            end
        end
    end
    return true
end


test_cases = [
    {
        pattern: "abba",
        s: "dog cat cat dog",
        expect: true
    },
    {
        pattern: "abba",
        s: "dog cat cat fish",
        expect: false
    },
    {
        pattern: "aaaa",
        s: "dog cat cat dog",
        expect: false
    },
    {
        pattern: "abba",
        s: "dog dog dog dog",
        expect: false
    },
]

for test_case in test_cases
    result = word_pattern(test_case[:pattern], test_case[:s])
    if result == test_case[:expect]
        print("Pass!\n")
    else
        print("Not pass, result #{result}\n")
    end
end