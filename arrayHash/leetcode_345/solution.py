class Solution:
    def reverseVowels(self, s: str) -> str:

        def reverseTwoStr(s, l, r, l_str, r_str):
            return s[:l] + r_str + s[l+1:r] + l_str + s[r+1:]



        l, r = 0, len(s) - 1
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        l_temp = ""
        r_temp = ""
        
        while l < r:
            if s[l] in vowels:
                l_temp = s[l]
            if s[l] not in vowels:
                l += 1
            if s[r] in vowels:
                r_temp = s[r]
            if s[r] not in vowels:
                r -= 1
            
            if l_temp != "" and r_temp != "":
                s = reverseTwoStr(s, l, r, l_temp, r_temp)
                l_temp = ""
                r_temp = ""
                l += 1
                r -= 1

        return s