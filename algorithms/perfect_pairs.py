from typing import List

class Solution:

    def perfectPairs(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                if min(abs(a - b), abs(a + b)) <= min(abs(a), abs(b)) and max(abs(a - b), abs(a + b)) >= max(abs(a), abs(b)):
                    res.append([i, j])

        return len(res)


obj = Solution()
nums = [-3,2,-1,4]

print(obj.perfectPairs(nums))