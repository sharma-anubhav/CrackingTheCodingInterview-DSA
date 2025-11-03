def solveNQueens(n):
    board = [["."] * n for _ in range(n)]
    res = []

    def is_safe(row, col):
        # Check column
        for r in range(row):
            if board[r][col] == "Q":
                return False

        # Check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # Check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True


    def backtrack(row):
        """
        We want to try and place a queen in each row. we check col by col to find safe col.
        ONce we get a col, we move to next row. 
        But another col might also be tehre in that same row that was not explored because we found one early
        so after we backtrack too.
        """
        if row == n:
            # Found a valid placement
            res.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."  # backtrack

    backtrack(0)
    return res
