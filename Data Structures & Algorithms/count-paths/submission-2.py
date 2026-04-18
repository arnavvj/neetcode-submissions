class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 and n == 1:
            return 1

        ans = []
        for i in range(0,m):
            ans.append([0 for i in range (0,n)])

        
        for i in range(1,m):
            ans[i][0] = 1

        for i in range(1,n):
            ans[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] += ans[i-1][j] + ans[i][j-1]

        return ans[-1][-1] 
        