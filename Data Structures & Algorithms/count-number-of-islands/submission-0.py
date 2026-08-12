class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        
        def dfs(r, c):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == '0'):
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)        
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    num_of_islands += 1

        return num_of_islands