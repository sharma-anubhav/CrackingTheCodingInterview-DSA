grid =  [[1, 5, 3],
         [4,-1, 0],
         [2, 0, 2]]

Output: [[5, 5, 3],
         [4, 2, 2],
         [2, 2, 2]]


## NAIVE SOLN (we can optimze this using dp)
def get_max(r, c, board):
    max_now = -1*float("inf")
    for cur_r in range(r, len(board)):
        for cur_c in range(c, len(board)):
            max_now = max(max_now, board[cur_r][cur_c])
    return max_now
    
def max_subgrid(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = get_max(r, c, board)

    for row in board:
        print(row)
    return board

max_subgrid(grid)









