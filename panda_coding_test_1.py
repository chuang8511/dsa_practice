import pdb

def solution(riddle):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    idx = 0
    for c in riddle:
        if c == "?":
            if len(result) == 0:
                previous_word = ""
            else:
                previous_word = result[-1]

            if idx+1 < len(riddle):
                next_word = riddle[idx+1]
            else:
                next_word = ""

            for alphabet in alphabets:
                if previous_word != alphabet and next_word != alphabet:
                    result += alphabet
                    break
        
        else:
            result += c
        
        idx += 1
    return result

print(solution("ab?ac?"))
print('==')
print(solution("????????"))
print('==')
print(solution("rd?e?wg??"))