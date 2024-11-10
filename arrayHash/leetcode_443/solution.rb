# @param {Character[]} chars
# @return {Integer}
def compress(chars)
    i = 0
    write = 0

    while i < chars.length
        char = chars[i]
        count = 0
        while i < chars.length and char == chars[i]
            i += 1
            count += 1
        end

        chars[write] = char
        write += 1

        if count > 1
            for count_str in count.to_s.split("")
                chars[write] = count_str
                write += 1
            end
        end
    end

    return write

end