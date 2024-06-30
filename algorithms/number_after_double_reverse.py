class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = str(num)[::-1]
        reversed2 = str(int(reversed1))[::-1]
        if int(reversed2) == num:
            return True
        return False


obj = Solution()
print(obj.isSameAfterReversals(526))
