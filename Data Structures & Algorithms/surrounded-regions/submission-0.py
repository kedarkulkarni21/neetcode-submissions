class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return

            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T": 
                    board[i][j] = "O"