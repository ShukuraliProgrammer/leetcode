from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        right = True
        right_count = 0
        left_count = 0
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] > 0 and right:
                right_count += 1
                continue
            elif arr[i+1] - arr[i] < 0:
                left_count += 1
                right = False
            else:
                return False
        if right_count ==0  or left_count == 0:
            return False

        return True


obj = Solution()
arr = [0, 3, 2,1]
print(obj.validMountainArray(arr))