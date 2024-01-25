from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        opt = 0
        count = Counter(nums)

        print("nums: ", nums)
        for k, v in count.items():
            print(k, v)
            if v == 1:
                return -1
            opt += v // 3
            if v % 3 != 0:
                opt += 1


        return opt


obj = Solution()
print(obj.minOperations([14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]))
