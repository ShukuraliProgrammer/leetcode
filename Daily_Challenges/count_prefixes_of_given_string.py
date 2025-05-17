from typing import List
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        for s_item in range(1, len(s)+1):
            print(s[:s_item])
            if s[:s_item] in words:

                counter += words.count(s[:s_item])

        return counter


count_pref = Solution()
words = ["a","b","c","ab","bc","abc"]
s = "abc"

print(count_pref.countPrefixes(words, s))