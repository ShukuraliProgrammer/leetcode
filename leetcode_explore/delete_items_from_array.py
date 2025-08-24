from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        while val in nums:
            nums.remove(val)
            nums.append("_")
            counter += 1

        return len(nums) - counter




obj = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2

print(obj.removeElement(nums, val))