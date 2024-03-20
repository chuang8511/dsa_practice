class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        line_length = 0
        i = 0
        self.collected_words = [[]]
        self.res = []
        
        while i < len(words):
            line_length += len(words[i]) + 1
            self.collected_words[-1].append(words[i])
            i += 1

            if i == len(words):
                break

            if line_length + len(words[i]) > maxWidth:
                self.collected_words.append([])
                line_length = 0
        
        # print(self.collected_words)

        for k, line_words in enumerate(self.collected_words):
            if k == len(self.collected_words) - 1:
                justified_sentences = ""
                for j, line_word in enumerate(line_words):
                    justified_sentences += line_word
                    if j != len(line_words) - 1:
                        justified_sentences += " "

                while len(justified_sentences) < maxWidth:
                    justified_sentences += " "
                
                self.res.append(justified_sentences)
                break


            space_count = len(line_words) - 1
            words_len = 0
            
            for line_word in line_words:
                words_len += len(line_word)
            
            space_len = maxWidth - words_len

            justified_sentences = ""

            if space_count == 0:
                justified_sentences += line_words[0]
                while len(justified_sentences) < maxWidth:
                    justified_sentences += " "

            elif space_len % space_count == 0:
                for j, line_word in enumerate(line_words):
                    justified_sentences += line_word
    
                    if j != len(line_words) - 1:
                        justified_sentences += (space_len // space_count) * " "
            else:
                remain_space = space_len % space_count
                for j, line_word in enumerate(line_words):
                    justified_sentences += line_word 
                    
                    if j != len(line_words) - 1:
                        justified_sentences += (space_len // space_count) * " "
                    
                    if remain_space != 0:
                        justified_sentences += " "
                        remain_space -= 1

            self.res.append(justified_sentences)    
            
        # print(self.res)
        return self.res