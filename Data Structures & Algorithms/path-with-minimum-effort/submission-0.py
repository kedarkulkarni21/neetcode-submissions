class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        min_heap = [[0, 0, 0]]
        visited = set()

        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            if (r == ROWS - 1) and (c == COLS - 1):
                return diff

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                new_r = dr + r
                new_c = dc + c

                if (new_r < 0) or (new_c < 0) or (new_r == ROWS) or (new_c == COLS):
                    continue
                
                new_diff = max(diff, abs(heights[r][c] - heights[new_r][new_c]))
                heapq.heappush(min_heap, [new_diff, new_r, new_c])
 
