from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        min_word = min(words)
        words.remove(min_word)

        res = []

        for letter in min_word:
            print("char: ", letter)
            for word in words:
                print("words: ", word)
                if letter in word:
                    print("word: ", word)
                    print("char in word: ", letter)
                    word.replace(letter, "", 1)
                    print("word: ", word)
                    continue
                else:
                    break
            res.append(str(letter))

        print("Res: ", res)
        return res

obj = Solution()
obj.commonChars(["bella","label","roller"])