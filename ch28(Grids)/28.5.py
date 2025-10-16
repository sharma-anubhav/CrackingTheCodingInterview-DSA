board = [
        [5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 0, 5, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 8, 0, 2, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7]
]

def check_box_elements(box_r, box_c, box_s, board):
    s = set()
    for r in range(box_r, box_r+box_s):
        for c in range(box_c, box_c+box_s):
            if board[r][c] in s and board[r][c]!=0:
                return False
    return True

def check_boxes(board, box_s):
    for r in range(0, len(board), box_s):
        for c in range(0, len(board[0]), box_s):
            if not check_box_elements(r, c, box_s, board):
                print("Box Check failed for:" , r, c)
                return False
    return True
    
            
def check_row_elements(board):
    for r in range(len(board)):
        s = set()
        for c in range(len(board[0])):
            if board[r][c] in s and board[r][c]!=0:
                print("Row Check failed for:" , r, " Found: ", board[r][c])
                return False
            s.add(board[r][c])            
    return True

def check_col_elements(board):
    for c in range(len(board[0])):
        s = set()
        for r in range(len(board)):
            if board[r][c] in s and board[r][c]!=0:
                print("Col Check failed for:" , c)
                return False
            s.add(board[r][c])            
    return True
    
def valid_sudoku(board):
    if check_boxes(board, 3) and check_row_elements(board) and check_col_elements(board):
        return True
    return False
    
print(valid_sudoku(board))












    