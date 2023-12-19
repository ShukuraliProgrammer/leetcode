from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
    row_count = len(mat)
    res = 0
    for i in range(row_count):
        for j in range(len(mat[i])):
            if j==i:
                res += mat[i][j]
    for i in range(row_count):
        for j in range(len(mat[i])):
            if i + j == len(mat[i])-1:
                if mat[i][j] == mat[len(mat[i])//2][len(mat)//2]:
                    pass
                else:
                    res += mat[i][j]
    return res

res = diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
print("Res: ",res)