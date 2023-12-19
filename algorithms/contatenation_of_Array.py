from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    res = []
    for i in nums:
        res.append(i)
    return nums + res

nums = [1,2,3,4]
res = getConcatenation(nums)
print(res)