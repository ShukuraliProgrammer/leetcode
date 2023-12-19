from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for number in nums:
            count = 0
            for number2 in range(len(nums)):
                if number > nums[number2]:
                    count += 1
            print(count)
            result.append(count)
        return result

obj = Solution()
nums = [6,5,4,8]
res = obj.smallerNumbersThanCurrent(nums)
print(res)


# Optimized Version
# coming soon



