import collections

def firstUniqChar(s: str) -> int:
    counter = collections.Counter(s)
    for key, val in counter.items():
        if val == 1:
            return s.index(key)
        else:
            continue
    return -1
res = firstUniqChar("leetcode")
print(res)
