from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common()[-1][0]

obj = Solution()
print(obj.singleNumber([2,2,1]))