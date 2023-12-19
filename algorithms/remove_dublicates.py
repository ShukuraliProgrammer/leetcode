from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed =set(nums)
        print(removed)
        return len(removed)

obj = Solution()
print(obj.removeDuplicates([1,1,2]))