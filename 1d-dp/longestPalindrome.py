class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [""]
        resLen = [0]

        def is_palindrome_and_valid_length(l, r):
            return l >= 0 and r < len(s) and s[l] == s[r]
        
        def loop_search_longest_palindrome(l, r):
            while is_palindrome_and_valid_length(l, r):
                length = r - l + 1
                if length > resLen[0]:
                    res[0] = s[l:r+1]
                    resLen[0] = length
                r += 1
                l -= 1

        for i in range(len(s)):
            # palindrome is odd-length string
            l, r = i, i
            loop_search_longest_palindrome(l, r)
            

            # palindrome is even-length string    
            l, r = i, i + 1
            loop_search_longest_palindrome(l, r)
            
        return res[0]
    
s = "babad"
solution = Solution()
solution.longestPalindrome(s)