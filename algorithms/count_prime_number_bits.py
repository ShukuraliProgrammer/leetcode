import math

left = int(input())
right = int(input())

items_range = [i for i in range(left, right + 1)]


def define_prime(number: int) -> int:
    sta = 1
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):  # range[2,sqrt(num)]
        if number % i == 0:
            sta = 0
            break
        else:
            continue
    if sta == 1:
        return True
    return False


sum_prime = 0
for x in items_range:
    num = bin(x).count('1')
    res = define_prime(num)
    if res:
        sum_prime += 1
    else:
        continue

print("items: ", items_range)
print("bits: ", sum_prime)
