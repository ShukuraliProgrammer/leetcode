from typing import List
from collections import Counter
def countBits(n: int) -> List[int]:
    res = [0]
    for i in range(1, n + 1):
        number = bin(i)
        print("number:" ,number)
        list_bits = [i for i in str(number)]
        c = Counter(list_bits)
        res.append(c["1"])
    return res

res = countBits(n=5)
print(res)