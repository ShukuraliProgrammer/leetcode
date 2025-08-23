def reverseString(s: list) -> list:
    len_s = len(s)
    s_copy = s.copy()
    for i in range(len_s):
        s[i], s[len_s - 1 - i] = s[len_s - 1 - i], s[i]

        if s_copy == s[::-1]:
            return s

    return []


print(reverseString(["h","e","l","l","o"]))