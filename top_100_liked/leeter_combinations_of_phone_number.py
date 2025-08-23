from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_letter_mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        results = []
        if len(digits) > 0:
            if len(digits) == 1:
                return number_letter_mappings[digits[0]]

            elif len(digits) == 2:
                combinations_count = len(number_letter_mappings[digits[0]]) * len(number_letter_mappings[digits[1]])
                for i in number_letter_mappings[digits[0]]:
                    for j in number_letter_mappings[digits[1]]:
                        mapping = str(i + j)
                        results.append(mapping)


            elif len(digits) == 3:
                for i in number_letter_mappings[digits[0]]:
                    for j in number_letter_mappings[digits[1]]:
                        for k in number_letter_mappings[digits[2]]:
                            mapping = str(i + j + k)
                            results.append(mapping)


            elif len(digits) == 4:
                for i in number_letter_mappings[digits[0]]:
                    for j in number_letter_mappings[digits[1]]:
                        for k in number_letter_mappings[digits[2]]:
                            for l in number_letter_mappings[digits[3]]:
                                mapping = str(i + j + k + l)
                                results.append(mapping)

            else:
                pass

            return results


        return []





obj = Solution()
print(obj.letterCombinations('23'))