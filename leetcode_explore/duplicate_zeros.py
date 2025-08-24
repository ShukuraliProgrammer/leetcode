from typing import List
import copy

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        counter = 0
        arr2 = []
        for i in range(len(arr)):
            if arr[i] == 0:
                arr2.append(0)
                counter += 1
                arr2.append(0)
            else:
                arr2.append(arr[i])

        for i in range(counter):
            arr2.pop()

        return arr2


obj = Solution()
arr = [1,0,2,3,0,4,5,0]
print(obj.duplicateZeros(arr))