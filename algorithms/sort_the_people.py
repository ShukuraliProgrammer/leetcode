from typing import List
def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    res = []
    for i in range(len(heights)):
        max_item = max(heights)
        res.append(names.pop(heights.index(max_item)))
        heights.remove(max_item)
    return res

names = ["Mary","John","Emma"]
heights = [180,165,170]

res = sortPeople(names, heights)
print("res: ", res)