class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND, ROWS, COLS = set(), len(grid), len(grid[0])

        def island(grid, row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in LAND or grid[row][col] != "1"):
                return
            LAND.add((row, col))
            island(grid, row + 1, col)
            island(grid, row - 1, col)
            island(grid, row, col + 1)
            island(grid, row, col - 1)

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in LAND and grid[row][col] == "1":
                    island(grid, row, col)
                    islands += 1
        return islands