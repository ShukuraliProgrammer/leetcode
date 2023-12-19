def numJewelsInStones(jewels: str, stones: str) -> int:
    res = 0
    for i in jewels:
        count = stones.count(i)
        res += count

    return res

jewels = "z"
stones = "ZZ"
res = numJewelsInStones(jewels, stones)
print("Res: ",res)