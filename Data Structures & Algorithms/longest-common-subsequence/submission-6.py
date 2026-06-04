class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        mat = [[None for i in range (len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text2) + 1):
            mat[-1][i] = 0

        for j in range(len(text1) + 1):
            mat[j][-1] = 0


        def recLCS(i, j):

            if mat[i][j] != None:
                return mat[i][j]

            if text1[i] == text2[j]:
                mat[i][j] = 1 + recLCS(i+1, j+1)

            else:
                mat[i][j] =  max(
                    recLCS(i+1, j),
                    recLCS(i, j+1)
                )

            return mat[i][j]


        return recLCS(0, 0)

            