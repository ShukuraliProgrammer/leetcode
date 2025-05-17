from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid.sort()
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        minimize_element = grid[0][0] + x
        operations = 0
        for grid_i in grid:
            for grid_j in grid_i:
                if grid_j % 2 == 1 and x % 2 == 0:
                    return -1
                while grid_j != minimize_element:
                    print(grid_i, grid_j)

                    if grid_j < minimize_element:
                        grid_j += x
                    elif grid_j > minimize_element:
                        grid_j -= x
                    else:
                        print(grid_j)
                        break

                    operations += 1
        print(operations)
        return operations
res = Solution()
grid = [[146]]
x = 86
print(res.minOperations(grid, x))



