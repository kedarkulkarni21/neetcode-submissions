class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(i, j):
            if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0):
                return 0

            grid[i][j] = 0
            return (1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1))

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area

