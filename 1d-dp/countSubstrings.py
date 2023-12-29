class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [0]
        def is_palindrome_and_valid_length(l, r):
            return l >= 0 and r < len(s) and s[l] == s[r]
        
        # def loop_possible_palindrome(l, r):
            
                

        for i in range(len(s)):
            # palindrome is odd-length string
            l, r = i, i
            while is_palindrome_and_valid_length(l, r):
                res[0] += 1
                l -= 1
                r += 1

            # palindrome is even-length string
            l, r = i, i + 1
            while is_palindrome_and_valid_length(l, r):
                res[0] += 1
                l -= 1
                r += 1
        return res[0]
            
            
            