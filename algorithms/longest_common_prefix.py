from typing import List
from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = Counter(strs)
        min_item = min(counter.items(), key=lambda x: x[1])
        res = ""
        k=0
        m = zip(*strs)
        for i in m:
            print("i: ", i)
        print("sds", m)
        print(min_item)
        print("min:", min_item)
        for i in min_item[0]:
            print("i:", i)
            if -1 not in [j.find(i) for j in strs]:
                res.append(i)
                continue
            else:
                break
        print("Res: ", res)
        return "".join(res)

obj = Solution()
print(obj.longestCommonPrefix(strs= ["aa", "ac"]))

