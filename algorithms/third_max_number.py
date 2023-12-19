from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_s = set(nums)
        print("nums_s", nums_s)
        first_m = max(nums_s)
        nums_s.remove(first_m)

        if nums_s:
            second_m = max(nums_s)
            nums_s.remove(second_m)
            if nums_s:
                third_m = max(nums_s)
                if third_m:
                    return third_m
                else:
                    return first_m


obj = Solution()
print(obj.thirdMax([2,2,3,1]))