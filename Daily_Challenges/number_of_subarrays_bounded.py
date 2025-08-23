from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start_index, end_index = 0, 0
        result = 0
        l = len(nums)
        for i in range(l):
            end_index = i
            print(start_index, end_index, nums[i], max(nums[start_index:end_index+1]))
            if left <= nums[i] <= right:
                result += 1
            elif left <= nums[start_index:end_index+1][0] <= right:
                result += 1
            else:
                start_index = i
            print('Start index: ', start_index)
            print("R: ", result)
        return result

s = Solution()
print(s.numSubarrayBoundedMax([2,9,2,5,6], 2, 8))