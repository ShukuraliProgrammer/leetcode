class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum([i for i in range(1, n + 1) if i % m == 0])
        num2 = sum([i for i in range(1, n + 1) if i % m != 0])
        print(num1, num2)
        return abs(num1 - num2)


obj = Solution()
print(obj.differenceOfSums(10, 3))