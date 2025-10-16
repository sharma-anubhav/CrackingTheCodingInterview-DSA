class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.r = len(matrix)
        self.c = len(matrix[0])

    def transpose(self):
        for i in range(self.r):
            for j in range(i):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        return

    def h_reflect(self):
        for row in self.matrix:
            row.reverse()

    def v_reflect(self):
        for i in range(self.c):
            u,d = 0, self.r-1
            while d>u:
                self.matrix[d][i], self.matrix[u][i] = self.matrix[u][i], self.matrix[d][i]
                u+=1
                d-=1
                
    def r_clock(self):
        self.transpose()
        self.h_reflect()
        return

    def r_c_clock(self):
        self.transpose()
        self.v_refelct()
        return
        
    def print(self):
        for row in self.matrix:
            print(row)

grid = [[1, 2],
        [3, 4]]
m = Matrix(grid)
m.print()
m.transpose()
m.print()
m.h_reflect()
m.print()
m.v_reflect()
m.print()
m.r_clock()
m.print()











        