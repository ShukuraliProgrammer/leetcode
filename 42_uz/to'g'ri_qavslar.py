def is_valid(s: str) -> bool:
    s_list = list(s)
    print(s_list)
    l_counter = 0
    r_counter = 0
    for i in range(len(s)):
        if "(" == s[i]:
            l_counter += 1
        else:
            r_counter += 1

        if l_counter >= r_counter:
            continue
        else:
            return False

    print(l_counter, r_counter)
    if l_counter == r_counter:
        return True

    return False




print(is_valid("((()()"))