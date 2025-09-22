def numberToWords(num: int) -> str:
    numbers_dict = {
        1: 'bir',
        2: 'ikki',
        3: 'uch',
        4: "to'rt",
        5: 'besh',
        6: 'olti',
        7: 'yetti',
        8: 'sakkiz',
        9: "to'qqiz"
    }
    onli_number_dict = {
        1: "o'n",
        2: 'yigirma',
        3: "o'ttiz",
        4: "qirq",
        5: 'ellik',
        6: 'oltmish',
        7: 'yetmish',
        8: 'sakson',
        9: "to'qson"
    }
    result = set()
    i = 0
    while 0 < num:
        var = num % 10
        i += 1
        if i == 1:
            result.add(numbers_dict[var])
        elif i == 2:
            result.add(onli_number_dict[var])
        elif i == 3:
            result.add(f"{numbers_dict[var]} yuz")
        elif i == 4:
            result.add(f"{numbers_dict[var]} ming")
        elif i == 5:
            result.add(f"{onli_number_dict[var]} ming")
        elif i == 6:
            result.add(f"{numbers_dict[var]} yuz ming")
        elif i == 7:
            result.add(f"{numbers_dict[var]} million")
        elif i == 8:
            result.add(f"{onli_number_dict[var]} million")
        elif i == 9:
            result.add(f"{numbers_dict[var]} yuz million")
        elif i == 10:
            result.add(f"{onli_number_dict[var]} milliard")

        num //= 10
    return " ".join(result)

num = 12345
print(numberToWords(num))
