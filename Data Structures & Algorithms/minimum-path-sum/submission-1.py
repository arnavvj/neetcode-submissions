"""
    [1,2,0] i
    [5,4,2] i
    [1,1,3] i
     i i i  i

    [N,N,N] i
    [N,N,N] i
    [N,N,3] i
     i i i  i
"""

class Solution:

    def recMPS(self, r, c):
        if self.gc[r][c] != None:
            return self.gc[r][c]

        # still exploring
        if self.gc[r][c+1] == None:
            self.recMPS(r, c+1)
        if self.gc[r+1][c] == None:
            self.recMPS(r+1, c)

        self.gc[r][c] = min(
            self.grid[r][c] + self.gc[r][c+1],
            self.grid[r][c] + self.gc[r+1][c]
        )

        return self.gc[r][c]


    def minPathSum(self, grid: List[List[int]]) -> int:
        
        gcopy = []
        for row in grid:
            rc = [None for n in row]
            rc.append(float('inf'))
            gcopy.append(rc)
        
        lr = [float('inf') for n in gcopy[0]]
        gcopy.append(lr)
        gcopy[-2][-2] = grid[-1][-1]
        gcopy[0][0] = grid[0][0]
        
        self.gc = gcopy
        self.grid = grid

        
        if self.gc[0][1] == None:
            self.recMPS(0, 1)
        if self.gc[1][0] == None:
            self.recMPS(1, 0)

        self.gc[0][0] = min(
            self.grid[0][0] + self.gc[0][1],
            self.grid[0][0] + self.gc[1][0]
        )

        if self.gc[0][0] == float('inf'):
            return grid[0][0]

        return self.gc[0][0]



