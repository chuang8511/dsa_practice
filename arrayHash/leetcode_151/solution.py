class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split()
        word_list.reverse()
        return " ".join(word_list)
        