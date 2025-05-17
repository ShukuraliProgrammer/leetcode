from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        nums_counter = Counter(nums)
        sorted_list = sorted(nums_counter.elements())
        formatted_str = str(sorted_list).replace(", ", ",")
        print("sorted list: ", formatted_str)
        return formatted_str


s = Solution()
print(s.sortColors([2,0,2,1,1,0]))
