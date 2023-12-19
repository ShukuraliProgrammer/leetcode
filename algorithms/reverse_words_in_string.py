def reverseWords(s: str) -> str:
    res = ""
    words = s.split()
    print("words: ", words)
    for word in words:
        res += word[::-1] + " "
    return res.strip()
s = "Let's take LeetCode contest"
res = reverseWords(s)
print("Res:", res)
