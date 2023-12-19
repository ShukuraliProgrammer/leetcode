from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            min_list = nums2
            max_list = nums1
        else:
            min_list = nums1
            max_list = nums2

        for i in min_list:
            if i in max_list:
                item = max_list.pop(max_list.index(i))
                res.append(item)
        return res


obj = Solution()
print(obj.intersect([4,9,5], [9,4,9,8,4]))
