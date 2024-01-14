# For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
# (i.e., t is concatenated with itself one or more times).
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        if str2[:len(str1)] != str1:
            return ""

        return self.gcdOfStrings(str1, str2[len(str1):])