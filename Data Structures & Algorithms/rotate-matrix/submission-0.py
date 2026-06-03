import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        i = 0
        n = len(matrix)

        while(i < n // 2):

            # used only for 
            # setting up the code in the loop with an example
            # i = 1

            # t = copy.deepcopy(matrix[i][i:n-i])                   # deep copy top
            t = copy.deepcopy(matrix[i][i:n-i])
            
            # r = copy.deepcopy(matrix[i:n-i][n-i-1] [::-1])        # deep copy right
            r = [matrix[j][n-i-1] for j in range(i,n-i)][::-1]

            # b = copy.deepcopy(matrix[n-i-1][i:n-i])               # deep copy bottom
            b = copy.deepcopy(matrix[n-i-1][i:n-i])

            # l = copy.deepcopy(matrix[i:n-i][n-i-1] [::-1])        # deep copy left
            l = [matrix[j][i] for j in range(i,n-i)][::-1]

            matrix[i][i:n-i] = l            # top becomes left
            
            for j in range(i, n-i):
                matrix[j][n-i-1] = t[j-i]   # right becomes top
            
            matrix[n-i-1][i:n-i] = r        # bottom becomes right
            
            for j in range(i, n-i):         # left becomes bottom
                matrix[j][i] = b[j-i]

            i += 1
            del(t, r, b, l)       


"""
        0   1   2   3   4
      .------------------
    0 | 1   2   3   4   5
      |
    1 | 1   2   3   4   5
      |
    2 | 1   2   3   4   5
      |
    3 | 1   2   3   4   5
      |
    4 | 1   2   3   4   5
"""