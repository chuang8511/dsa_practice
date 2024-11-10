def reverse_words(s)

    words = s.split(" ")

    result = ""
    i = words.length - 1

    while i >= 0
        word = words[i]
        if i == words.length - 1
            result = word
        else
            result += " " + word
        end
        i -= 1
    end

    return result
end

test_cases = ["the sky is blue"]

for test_case in test_cases
    print(reverse_words(test_case))
end
