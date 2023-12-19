from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return digit_map[digits]
        results = []
        for i in range(1, len(digits)):
            for j in range(i+1, len(digits)):
                print("i: ", digit_map[i], "j: ", digit_map[j])
                results.append(digit_map[i]+digit_map[j])

        return results

obj = Solution()
print(obj.letterCombinations("23"))