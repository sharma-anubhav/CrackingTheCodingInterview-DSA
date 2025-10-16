## GOOD
def is_valid(r, c, board):
    if 0<=r<len(board) and 0<=c<len(board) and board[r][c] == 0:
        return True
    return False

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def spiral(n):
    board = [[0]*n for i in range(n)]
    num = n*n-1
    cur_r, cur_c = n-1, n-1
    direction = 0
    
    while num >= 0:
        ## ALWAYS TAKE SINGLE STEPS INSIDE A WHILE LOOP TO PREVENT COMPLICATIONS
        if is_valid(cur_r, cur_c, board):
            board[cur_r][cur_c] = num
            num-=1
            cur_r, cur_c = cur_r+directions[direction][0], cur_c+directions[direction][1]
        else:
            cur_r, cur_c = cur_r-directions[direction][0], cur_c-directions[direction][1]
            direction = (direction+1)%4
            cur_r, cur_c = cur_r+directions[direction][0], cur_c+directions[direction][1]

    for row in board:
        print(row)
    return board

spiral(7)

## CORRECT BUT BAD (can get hard to visualize edge cases)
def spiral(n):
    s = [[0]*n for i in range(n)]
    cur_r, cur_c = n-1, n-1
    i = n*n-1
    
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    direction = 0

    while i >= 0:
        while is_valid(cur_r, cur_c, s, n):
            s[cur_r][cur_c] = i
            i-=1
            cur_r, cur_c = cur_r+directions[direction][0], cur_c+directions[direction][1]
        
        cur_r, cur_c = cur_r-directions[direction][0], cur_c-directions[direction][1]
        direction = (direction+1)%4
        cur_r, cur_c = cur_r+directions[direction][0], cur_c+directions[direction][1]

