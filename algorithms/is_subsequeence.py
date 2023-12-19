def isSubsequence(s: str, t: str) -> bool:
    res = True
    for step in s:
        if step in t:
            continue
        else:
            res = False
    return res


s = "axc"
t = "ahgbdc"
res = isSubsequence(s, t)
print(res)
