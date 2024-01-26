from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        length = len(arr)
        odd_numbers = [i for i in range(length) if i % 2 != 0]
        res = []

        if length < 3:
            return sum(arr)

        for i in odd_numbers:
            sub_arrays = []

            for j in range(length - i + 1):
                sub_arrays.append(sum(arr[j:j + i]))
            res.append(sum(sub_arrays))
        if length % 2 != 0:
            res.append(sum(arr))

        return sum(res)


obj = Solution()
print(obj.sumOddLengthSubarrays([7,6,8,6]))
