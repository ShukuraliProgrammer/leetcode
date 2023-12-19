from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lesftSum = []
        answer = []
        for i in range(len(nums)):
            if i == 0:
                lesftSum.append(0)
            else:
                lesftSum.append(sum(nums[:i]))
        return answer

obj = Solution()
print(obj.leftRightDifference([1,2,3,4,5]))
