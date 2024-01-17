# from collections import defaultdict
# class Solution:
#     def compress(self, chars: list[str]) -> int:
#         word_dic = defaultdict(int)
#         s = ""
#         for c in chars:
#             word_dic[c] += 1

#         chars = []
#         for key in word_dic.keys():
#             if word_dic[key] == 1:
#                 s = s + key
#                 chars.append(key)
#             else:
#                 s = s + key + str(word_dic[key])
#                 chars.append(key)
#                 chars.append(str(word_dic[key]))
#         return chars