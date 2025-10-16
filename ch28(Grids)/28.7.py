grid =  [[-1,  2,  3],
         [ 4,  0,  0],
         [-2,  0,  9]]
Output: [[15, 14, 12],
         [11,  9,  9],
         [ 7,  9,  9]]

# Again this is a naive solution and we can optimize this using Dp
def get_sum(r, c, board):
    sum = 0
    for cur_r in range(r, len(board)):
        for cur_c in range(c, len(board)):
            sum+=board[cur_r][cur_c]
    return sum
    
def sum_subgrid(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = get_sum(r, c, board)

    for row in board:
        print(row)
    return board

sum_subgrid(grid)


## OPtimizing this. It is similar to directions. form any point we have three posibilties to explore.
## we keep on exploring till we get to the top. 

def is_valid(r, c, n_r, n_c):
    if 0<=r<n_r and  0<=c<n_c:
        return True
        
def sum_subgrid(board):
    n_r, n_c = len(board), len(board[0])
           
    for r in range(n_r-1, -1, -1):
        for c in range(n_c-1, -1, -1):
            sum= 0
            sum+=board[r][c]
            if is_valid(r+1, c, n_r, n_c):
                sum+=board[r+1][c]
            if is_valid(r, c+1, n_r, n_c):
                sum+=board[r][c+1]
            if is_valid(r+1, c+1, n_r, n_c):
                sum-=board[r+1][c+1]
            board[r][c] = sum

    for row in board:
        print(row)
    return board

sum_subgrid(grid)










