from typing import List

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        n_lcm = 0
        sumOdd = -1
        sumOdd_sum = 0
        sumEven = 0
        sumEven_sum = 0
        res = 0
        if n == 1:
            return 1

        for i in range(1, n+1):
            sumOdd += 2
            sumOdd_sum += sumOdd

            sumEven += 2
            sumEven_sum += sumEven


        for i in range(1, sumOdd_sum//2 + 1):
            if sumOdd_sum % i == 0 and sumEven_sum % i == 0:

                res = max(res, i)

        return res


obj = Solution()
n = 5
print(obj.gcdOfOddEvenSums(n))