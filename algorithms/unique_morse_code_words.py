from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters_list = [chr(let) for let in range(ord('a'), ord('z')+1)]

        morse_list = [0, ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = []
        for word in words:
            converted_morse = []
            for letter in word:

                letter_index = letters_list.index(letter) + 1

                converted_morse.append(morse_list[letter_index])
            res.append("".join(converted_morse))
        return len(set(res))

obj = Solution()
print(obj.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))