from collections import defaultdict, Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        word_count = Counter(words)
        self.res = []

        for i in range(word_len):
            start = i 
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word not in word_count:
                    start = j + word_len
                    window = defaultdict(int)
                    words_used = 0
                    continue
                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start:start+word_len]] -= 1
                    start += word_len
                    words_used -= 1

                if words_used == len(words):
                    self.res.append(start)
        self.res.sort()
        return self.res