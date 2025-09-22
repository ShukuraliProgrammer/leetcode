from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        index_count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                index_count += 1
            else:
                continue
        return index_count
    
        
obj = Solution()
heights = [1,2,3,4,5]
print(obj.heightChecker(heights))  # Output: 3