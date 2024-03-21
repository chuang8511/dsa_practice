from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        l, m, r = 0, 0, word_len
        self.res = []
        
        word_counts = defaultdict(int)
        for word in words:
            word_counts[word] += 1

        compare_word_counts = defaultdict(int)
        # print(f"word count: {word_counts}")
        while r <= len(s):
            
            word = s[m:r]
            
            if word in words and compare_word_counts[word] < word_counts[word]:
                compare_word_counts[word] += 1
                r += word_len
                m += word_len
            else:
                l += 1
                m = l
                r = l + word_len
                compare_word_counts = defaultdict(int)

            
            # print(f"compare_word_counts: {compare_word_counts}")
            if compare_word_counts == word_counts:
                self.res.append(l)                
                compare_word_counts = defaultdict(int)
                l += 1
                m = l
                r = l + word_len
            
        return self.res