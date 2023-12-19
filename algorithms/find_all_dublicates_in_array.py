from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                res.append(nums[i])
                continue
        return res
obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))