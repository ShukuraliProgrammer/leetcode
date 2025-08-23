from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_counter = 0
        one_res = []
        if len(nums) < 2 and 1 not in nums:
            return 0


        for i in range(len(nums)):
            last_item = nums[i]
            if nums[i] == 1 and last_item == nums[i]:
                one_counter += 1
            else:
                one_counter = 0
            one_res.append(one_counter)
        return max(one_res)


obj = Solution()
nums = [1]
print(obj.findMaxConsecutiveOnes(nums))