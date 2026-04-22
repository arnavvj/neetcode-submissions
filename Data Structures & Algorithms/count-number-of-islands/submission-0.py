class Solution:

    def sinkIsland(self, i, j):
        if self.grid[i][j] == "1":

            self.grid[i][j] = "0"

            if i-1 >= 0:
                self.sinkIsland(i-1, j)
            if i+1 < len(self.grid):
                self.sinkIsland(i+1, j)
            if j-1 >= 0:
                self.sinkIsland(i, j-1)
            if j+1 < len(self.grid[0]):
                self.sinkIsland(i, j+1)

    def numIslands(self, grid: List[List[str]]) -> int:

        count, self.grid = 0, grid

        for i in range(len(self.grid)):
            for j in range(len(grid[0])):

                if self.grid[i][j] == "1":
                    self.sinkIsland(i, j)
                    count += 1

        return count
        