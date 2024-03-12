import string
from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.res = []
        if digits == "":
            return self.res
        
        int_alphabet_dict = self.build_dict()

        def backtracking(combination: str, next_digits: str) -> None:
            if not next_digits:
                self.res.append(combination)
                return
            
            for letter in int_alphabet_dict[next_digits[0]]:
                backtracking(combination + letter, next_digits[1:])
        
        backtracking("", digits)

        return self.res



    def build_dict(self) -> dict:
        int_alphabet_dict = defaultdict(str)
        i = 2
        counter = 0
        for chr in string.ascii_lowercase:
            if i in [7, 9]:
                if counter == 4:
                    i += 1
                    counter = 1
                else:
                    counter += 1
            elif counter == 3:
                i += 1
                counter = 1    
            else:
                counter += 1
            int_alphabet_dict[str(i)] += chr
        return int_alphabet_dict
        


    #     combination_dict = {}
        
    #     pointer_idx = 0
        
    #     for chr in digits:
    #         combination_dict[pointer_idx] = { "cur_point": 0 , "strings": int_alp_map[chr], "max_point": len(int_alp_map[chr]) - 1 }
    #         pointer_idx += 1



    #     while self.not_end(combination_dict):

    # def not_end(self, combination_dict: dict) -> bool:
    #     keys = combination_dict.keys()
        
    #     for i in keys:
    #         if combination_dict[i]["cur_point"] != combination_dict[i]["max_point"]:
    #             return True
        
    #     return False