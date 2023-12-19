from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

        return nums


obj = Solution()
print(obj.moveZeroes([0,0,1]))