# 1
# 1 1
# 1 2 1
# 1 3 3 1


def generate(n: int) -> list:
    results = []
    for i in range(0, n):
        res = [1] * (i+1)
        for j in range(1, i):
            res[j] = results[i-1][j-1] + results[i-1][j]
        results.append(res)
    return results



print(generate(4))