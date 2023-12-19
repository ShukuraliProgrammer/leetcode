def findTheDifference(s: str, t: str) -> str:
    if len(s) == 0:
        return t
    for index, (step_s, step_t) in enumerate(zip(s, t)):
        if step_s in t:
            t = t.replace(t[index], "", 1)
    return t

s = "ab"
t = "aab"
res = findTheDifference(s, t)
print("result: ", res)
