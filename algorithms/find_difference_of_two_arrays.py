from typing import List


class Solution:
    def find_difference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answers = []
        items_of_nums1 = []
        items_of_nums2 = []

        for item1, item2 in zip(nums1, nums2):


            if item1 in nums2:
                pass
            else:
                if not item1 in items_of_nums1:
                    items_of_nums1.append(item1)

            if item2 in nums1:
                continue
            else:
                if not item2 in items_of_nums2:
                    items_of_nums2.append(item2)

        answers.append(items_of_nums1)
        answers.append(items_of_nums2)
        return answers

obj = Solution()
res = obj.find_difference([1,2,3], [2,4,6])
print("res: ", res)