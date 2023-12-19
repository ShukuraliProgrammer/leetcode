def maximum69Number(num: int) -> int:
    s_num = list(str(num))
    res = []
    for n in range(len(s_num)):
        if all(int(x) == 9 for x in s_num):
            return num
        if int(s_num[n]) == 9:
            s_num[n]="6"
            res.append(int(''.join(s_num)))
            s_num[n]="9"

        elif int(s_num[n]) == 6:
            s_num[n]="9"
            res.append(int(''.join(s_num)))
            s_num[n]="6"

    return max([int(i) for i in res])


res = maximum69Number(9999)
print("res: ", res)
