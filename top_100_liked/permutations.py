from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) + 1
        r = len(nums)

        def find_factorial(number):
            multiple = 1
            for i in range(1, number):
                multiple *= i
            return multiple

        return find_factorial(n)//find_factorial(n - r)


obj = Solution()
nums = [1,2,3]
print(obj.permute(nums))