def balancedStringSplit(self, s: str) -> int:
    counter_of_R = counter_of_L = 0
    counter_of_substring = 0
    for step in s:
        if step == "R":
            counter_of_R += 1
        elif step == "L":
            counter_of_L += 1

        if counter_of_L == counter_of_R:
            counter_of_substring += 1

            counter_of_L = counter_of_R = 0

    return counter_of_substring
var = balancedStringSplit(s="RLRRLLRLRL")
print("var: ", var)
