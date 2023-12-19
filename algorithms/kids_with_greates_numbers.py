from typing import List
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    res = []
    for i in candies:
        print(min(candies))
        if min(candies) + extraCandies != (i + extraCandies):
            res.append(True)
        else:
            res.append(False)
    return res

res = kidsWithCandies([2,3,5,1,3], 3)
print("Resp: ", res)