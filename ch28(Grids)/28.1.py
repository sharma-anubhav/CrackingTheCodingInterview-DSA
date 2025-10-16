board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
piece = "king"
r = 3
c = 5


kq_directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)]
h_directions = [(2,1),(2,-1),(-2,1),(-2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]

def get_directions(piece):
    if piece == "king" or piece == "queen":
        return kq_directions
    return h_directions
    
def is_valid(r, c, grid):
    if 0<=r<= len(grid) and 0 <= c <= len(grid[0]) and grid[r][c]!=1:
        return True
    return False
    
def move(cur_r, cur_c, direction):        
    return cur_r + direction[0], cur_c + direction[1]
    
def possibilities(board, piece, r, c):
    directions = get_directions(piece)
    count = 0
    for direction in directions:
        cur_r, cur_c = r, c
        if piece == "queen":
            while is_valid(cur_r, cur_c, grid):
                cur_r, cur_c = move(cur_r, cur_c, direction)
                if is_valid(cur_r, cur_c, grid):
                    count+=1
        else:
            cur_r, cur_c = move(cur_r, cur_c, direction)
            if is_valid(cur_r, cur_c, grid):
                count+=1            
    return count
