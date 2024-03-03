# to be checked: https://leetcode.com/problems/evaluate-division/solutions/3543256/image-explanation-easiest-concise-complete-intuition-c-java-python/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        return
        # self.res = []
        

        # for query in queries:
        #     check_strings = set(query)
        #     len_strings = len(check_strings)
        #     numerator = query[0]
        #     denominator = query[1]
        #     product_arr = [] # [idx, should_reverse_boolean]
        #     self.ok_to_product = False
        #     self.already_append = False

        #     for idx, equation in enumerate(equations):
        #         nu, de = equation[0], equation[1]
        #         if len_strings == 1:
        #             if nu in check_strings or de in check_strings:
        #                 self.res.append(1.0)
        #                 self.already_append = True
        #                 break
                    
        #         else:
        #             if nu == numerator and de == denominator:
        #                 product_arr.append([idx, False])
        #                 self.ok_to_product = True
        #                 break
        #             elif nu == denominator and de == numerator:
        #                 product_arr.append([idx, True])
        #                 self.ok_to_product = True
        #                 break
        #             elif nu == numerator:
        #                 product_arr.append([idx, False])
        #                 numerator = de
        #             elif de == denominator:
        #                 product_arr.append([idx, False])
        #                 denominator = nu
        #             elif nu == denominator:
        #                 product_arr.append([idx, True])
        #                 denominator = de
        #             elif de == numerator:
        #                 product_arr.append([idx, True])
        #                 numerator = nu
        #             else:
        #                 pass
        #     if product_arr and self.ok_to_product:
        #         to_be_append_res = 1
        #         for arr in product_arr:
        #             val_idx, reverse = arr[0], arr[1]

        #             if reverse:
        #                 to_be_append_res *= 1 / values[val_idx]
        #             else:
        #                 to_be_append_res *= values[val_idx]
        #         self.res.append(to_be_append_res)
        #     elif self.already_append:
        #         pass
        #     else:
        #         self.res.append(-1.0)
        #     print(query)
        #     print(self.res)
        # return self.res