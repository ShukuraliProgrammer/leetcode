from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> list[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        return sorted(nums1)


obj = Solution()
print(obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
