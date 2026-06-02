class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        nrows, ncols = len(matrix), len(matrix[0])

        rows_hash = ""
        for i in range(nrows):
            rows_hash += "1"

        cols_hash = ""
        for i in range(ncols):
            cols_hash += "1"


        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    rows_hash = rows_hash[:i] + "0" + rows_hash[i+1:]
                    cols_hash = cols_hash[:j] + "0" + cols_hash[j+1:]

        print(rows_hash)
        print(cols_hash)

        for i in range(0, len(rows_hash)):
            if rows_hash[i] == "0":
                for j in range(ncols):
                    matrix[i][j] = 0

        for j in range(0, len(cols_hash)):
            if cols_hash[j] == "0":
                for i in range(nrows):
                    matrix[i][j] = 0
        