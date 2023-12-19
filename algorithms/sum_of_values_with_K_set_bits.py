from typing import List
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            bin_num = str(bin(i)).count("1")
            if bin_num == k:
                res.append(nums[i])

        return sum(res)

obj = Solution()
print(obj.sumIndicesWithKSetBits([5,10,1,5,2], 1))