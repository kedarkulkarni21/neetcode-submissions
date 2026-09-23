class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pac_grid = [[False] * num_cols for _ in range(num_rows)]
        atl_grid = [[False] * num_cols for _ in range(num_rows)]

        def bfs(sources, ocean_grid):
            q = deque(sources)
            while q:
                r, c = q.popleft()
                ocean_grid[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < num_rows and 0 <= nc < num_cols and not ocean_grid[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for c in range(num_cols):
            pacific.append((0, c))
            atlantic.append((num_rows - 1, c))

        for r in range(num_rows):
            pacific.append((r, 0))
            atlantic.append((r, num_cols - 1))

        bfs(pacific, pac_grid)
        bfs(atlantic, atl_grid)

        res = []
        for r in range(num_rows):
            for c in range(num_cols):
                if pac_grid[r][c] and atl_grid[r][c]:
                    res.append([r, c])

        return res
        