class Solution:
    def sumBase(self, n: int, k: int) -> int:
        remainder = []
        while n >= k:
            remainder.append(n % k)
            n //= k
        remainder.append(n)
        remainder.reverse()
        return sum(remainder)


obj = Solution()
print(obj.sumBase(10, 10))