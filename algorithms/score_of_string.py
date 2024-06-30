class Solution:
    def scoreOfString(self, s: str) -> int:
        ord_numbers = []
        summ = 0
        for i in s:
            ord_numbers.append(ord(i))
        for n in range(4):
            print("n", abs(ord_numbers[n] - ord_numbers[n+1]))
            summ += abs(ord_numbers[n] - ord_numbers[n+1])

        return summ

obj = Solution()
print(obj.scoreOfString("hello"))