# 1-step: s = "leet2code3" , numbers = [0]
# 2-step: s = "leetleet" , numbers = [0, 2]
# 3-step: s = leetleet, numbers = [0, 2, 3]

def decodeAtIndex(s: str, k: int) -> str:
    letters_col = ""
    string_until_digit = ""
    numbers = [0]
    for item in s:
        print("item: ", item)
        if item.isdigit():
            numbers.append(item)
            print("numbers: ", numbers[-1])
            if numbers[0] == 0 and len(numbers) == 2:
                print("index: ", s.find(item))
                string_until_digit += s[:s.find(item)]
            else:
                print("index: ", s.find(item))
                print("code: ", s[s.find(numbers[-2])+1:s.find(item)])
                letters_col += s[s.find(numbers[-2])+1:s.find(item)]
                string_until_digit = letters_col
            print("string untill digit: ", string_until_digit)
            item = int(item)
            for letter in range(item):
                letters_col += string_until_digit
                print("letters_col: ", letters_col)
        else:
            continue
    return letters_col

res = decodeAtIndex(s="ha6", k=5)

print("res: ", res)