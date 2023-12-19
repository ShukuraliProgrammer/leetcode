class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lowercase_alphabet = [chr(let) for let in range(ord('a'), ord('z') + 1)]
        print("lowercase_alphabet: ", lowercase_alphabet)
        for i in sentence:
            if i in lowercase_alphabet:
                lowercase_alphabet.remove(i)
            else:
                continue
        if len(lowercase_alphabet) == 0:
            has_letter = True
        else:
            has_letter = False
        return has_letter

obj = Solution()
print(obj.checkIfPangram("leetcode"))