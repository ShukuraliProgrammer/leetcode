from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def find_digits(num: int):
            return len(str(num))

        even_numer_counter = 0

        for num in nums:
            num_digits = find_digits(num)
            if num_digits % 2 == 0:
                even_numer_counter += 1
            else:
                continue

        return even_numer_counter





obj = Solution()
nums = [555,901,482,1771]
print(obj.findNumbers(nums))