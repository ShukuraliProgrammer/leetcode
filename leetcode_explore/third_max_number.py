from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = list(set(nums))
        print(distinct_nums)
        max_first = max(distinct_nums)
        distinct_nums.remove(max_first)
        second_max = max(distinct_nums) if distinct_nums else max_first
        print(distinct_nums)
        distinct_nums.remove(second_max) if distinct_nums else max_first
        print(distinct_nums)
        third_max = max(distinct_nums) if distinct_nums else max(max_first, second_max)

        if third_max:
            return third_max
        elif second_max:
            return second_max
        else:
            return max_first
        

obj = Solution()
nums = [1,2]
print(obj.thirdMax(nums))  # Output: 1