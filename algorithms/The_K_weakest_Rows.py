from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_count = []
        indexes = []
        for i in mat:
            soldiers_count.append(i.count(1))
        min_finder = soldiers_count.copy()
        print("soldiers_count",soldiers_count)
        while len(soldiers_count) > 1:
            index = soldiers_count.index(min(min_finder))
            print("item",index)
            min_finder.pop(index)
            print("poped: ", soldiers_count)
            indexes.append(index)
        return indexes[:k]

obj = Solution()
print(obj.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]],3))
