from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_pointer = 0
        max_length = 0
        last_zero = -1
        for i in range(len(nums)):

            if nums[i] == 0:
                left_pointer = last_zero + 1
                last_zero = i

            max_length = max(max_length, i - left_pointer)

        return max_length





obj = Solution()
nums = [1,1,0,1]
print(obj.longestSubarray(nums))