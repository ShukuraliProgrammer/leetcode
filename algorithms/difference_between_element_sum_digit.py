from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(int(digit) for digit in "".join(map(str, nums))))

obj = Solution()
print(obj.differenceOfSum([1,15,6,3]))