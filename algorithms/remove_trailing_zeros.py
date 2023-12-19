class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_list = list(map(int, num))
        while num_list[-1] == 0:
            num_list.pop()
            if num_list[i] == 0:
                num_list.pop(i)
            else:
                break
        return "".join(map(str, num_list))

obj = Solution()
print(obj.removeTrailingZeros("1230000"))