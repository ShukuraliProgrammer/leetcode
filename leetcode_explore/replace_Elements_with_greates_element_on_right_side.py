from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                return arr

            arr[i] = max(arr[i+1:])



obj = Solution()
arr = [17,18,5,4,6,1]
print(obj.replaceElements(arr))