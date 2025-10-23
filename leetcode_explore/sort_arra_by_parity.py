from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_index = -1
        odd_index = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_index = i

            elif nums[i] % 2 == 1:
                odd_index = i

            if even_index > odd_index:
                nums[i], nums[even_index] = nums[even_index], nums[i]


        print(nums)

        return nums

obj = Solution()
nums = [3,1,2,4]
print(obj.sortArrayByParity(nums))
