from collections import Counter

from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        counter = Counter(nums)
        max_frequency = max(counter.values())
        if max_frequency == 1:
            return len(nums)
        numbers = []
        for num, freq in counter.items():

            if freq == max_frequency:
                numbers.append(num)

        return max_frequency * len(numbers) if numbers else max_frequency


obj = Solution()
nums = [1,2,3,4,5]
print(obj.maxFrequencyElements(nums))