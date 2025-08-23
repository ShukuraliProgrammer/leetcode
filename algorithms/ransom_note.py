from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        ransom_counter = Counter(ransomNote)

        for letter in ransom_counter.elements():
            if letter in magazine:
                if magazine_counter[letter] >= ransom_counter[letter]:
                    continue
                else:
                    return False
            else:
                return False

        return True



obj = Solution()

ransomNote = "aa"
magazine = "aab"

print(obj.canConstruct(ransomNote, magazine))