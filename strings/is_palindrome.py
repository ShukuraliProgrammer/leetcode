from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i].isupper():
                res.append(s[i].lower())

            elif s[i].isalnum():
                res.append(s[i])

            else:
                continue



        return "".join(res)[::-1] == "".join(res)

obj = Solution()
s = "0P"
print(obj.isPalindrome(s))