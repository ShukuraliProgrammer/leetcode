class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_list = []
            summ = 0
            for item in range(len(s) - 1):
                summ = (int(s[item]) + int(s[item + 1])) % 10
                new_list.append(summ)
            s = "".join(map(str, new_list))
        return s == s[::-1]
    

obj = Solution()
s = "34789"
print(obj.hasSameDigits(s))
        