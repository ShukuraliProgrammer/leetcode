class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_n = 0
        mul_n = 1
        while n >= 10:
            q = n % 10
            n = n // 10
            mul_n *= q
            sum_n += q
            print(mul_n, sum_n, n)
        mul_n *= n
        sum_n += n
        print(mul_n, sum_n)
        return mul_n - sum_n


obj = Solution()
print(obj.subtractProductAndSum(10225))