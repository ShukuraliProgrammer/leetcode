from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count = len(mat)
        column_count = len(mat[0])
        total_iterations = row_count * column_count
        row_bool = False
        column_bool = False
        special_positions = 0
        for i in range(row_count):
            for j in range(column_count):

                if mat[i][j] == 1:
                    for z in range(row_count):
                        print("z: ", z, "j: ", j)
                        if mat[z][j] == 0:
                            print("mat[z][j]: ", mat[z][j])
                            row_bool = True
                            continue

                    for z in range(column_count):
                        if mat[i][z] == 0:
                            column_bool = True
                            continue

                    print("row_bool: ", row_bool, "column_bool: ", column_bool)
                    if row_bool and column_bool:
                        special_positions += 1
                    row_bool = False
                    column_bool = False
        return special_positions


obj = Solution()
print(obj.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
