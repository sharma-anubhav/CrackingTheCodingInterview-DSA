directions =  [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)]

def is_valid(r, c, board):
    if 0 <= r < len(board) and 0 <= c < len(board[0]):
        return True
    return False
    
def mark_locations(r, c, ans):
    for direction in directions:
        cur_r, cur_c = r, c
        while(is_valid(cur_r, cur_c, ans)):
            ans[cur_r][cur_c]=1
            cur_r, cur_c = cur_r+direction[0], cur_c+direction[1]
            
def k_queens(board):
    r_cnt, c_cnt = len(board), len(board[0])
    ans = [ [0 for _ in range(c_cnt)] for _ in range(r_cnt) ]
    for r in range(len(board)):
        for c in range(len(board[0])):    
            if board[r][c] == 1:
                mark_locations(r, c, ans)
    return ans

print(k_queens(board))