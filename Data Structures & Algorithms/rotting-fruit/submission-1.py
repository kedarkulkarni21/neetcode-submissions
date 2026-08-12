class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_oranges = 0
        mins = -1

        # count the number of fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if fresh_oranges == 0:
            return 0

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            mins += 1
            q_len = len(q)

            for _ in range(q_len):
                row, col = q.popleft()

                for x, y in dirs:
                    new_r = x + row
                    new_c = y + col

                    if (new_r >= 0 and new_c >= 0 and new_r < len(grid) and new_c < len(grid[0]) and grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 2
                        fresh_oranges -= 1
                        q.append((new_r, new_c))

        return mins if fresh_oranges == 0 else -1
        
            