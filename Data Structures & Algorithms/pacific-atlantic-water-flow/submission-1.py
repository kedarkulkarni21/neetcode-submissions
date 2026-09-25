class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac_grid = [[False] * COLS for _ in range(ROWS)]
        pacific_q = deque()
        atl_grid = [[False] * COLS for _ in range(ROWS)]
        atlantic_q = deque()

        def bfs(ocean_q, ocean_grid):
            while ocean_q:
                r, c = ocean_q.popleft()
                ocean_grid[r][c] = True
                for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr = x + r
                    nc = y + c
                    if (0 <= nr < ROWS and 0 <= nc < COLS and not ocean_grid[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        ocean_q.append((nr, nc))

        for c in range(COLS):
            pacific_q.append((0, c))
            atlantic_q.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific_q.append((r, 0))
            atlantic_q.append((r, COLS - 1))

        bfs(pacific_q, pac_grid)
        bfs(atlantic_q, atl_grid)

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if pac_grid[row][col] and atl_grid[row][col]:
                    res.append([row, col])

        return res
        