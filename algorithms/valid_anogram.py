from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_word = Counter(s)
        t_word = Counter(t)
        print(s_word, t_word)
        res = False
        letters_count = 0
        for item_t in t_word.keys():
            if t_word[item_t] == s_word[item_t]:
                letters_count += 1
                continue
            else:
                break
        print(letters_count, len(set(t)))
        if len(set(t)) == letters_count and len(set(s)) == letters_count:
            res = True
        return res

obj = Solution()
s = "ab"
t = "a"
print(obj.isAnagram(s, t))