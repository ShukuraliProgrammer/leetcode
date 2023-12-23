class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ways_possibility = {(0, 0)}
        x = 0
        y = 0

        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1

            if (x, y) in ways_possibility:
                return True
            else:
                ways_possibility.add((x, y))


        return False


obj = Solution()
print(obj.isPathCrossing("NNSWWEWSSESSWENNW"))
