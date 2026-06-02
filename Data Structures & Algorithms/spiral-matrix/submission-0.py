class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []

        turn = {
            'r': 'd',   # if going right, next go down
            'd': 'l',   # if going down, next go left
            'l': 'u',   # if going left, next go up
            'u': 'r'    # if going up, next go right
        }

        nrows, ncols = len(matrix), len(matrix[0])

        visited = [[0 for j in range(ncols)] for i in range(nrows)]
        vis_count = 0

        direction = 'r'
        i, j = 0, 0

        while (True):

            # when going right
            if direction == 'r':
                while(j < ncols):
                    if visited[i][j] == 1:
                        break
                    else:
                        ans.append(matrix[i][j])
                        visited[i][j] = 1
                        vis_count += 1
                        j += 1
            direction = turn[direction]
            i += 1
            j -= 1
            if vis_count == nrows * ncols:
                break


            # when going down
            if direction == 'd':
                while(i < nrows):
                    if visited[i][j] == 1:
                        break
                    else:
                        ans.append(matrix[i][j])
                        visited[i][j] = 1
                        vis_count += 1
                        i += 1
            direction = turn[direction]
            j -= 1
            i -= 1
            if vis_count == nrows * ncols:
                break


            # when going left
            if direction == 'l':
                while(j >= 0):
                    if visited[i][j] == 1:
                        break
                    else:
                        ans.append(matrix[i][j])
                        visited[i][j] = 1
                        vis_count += 1
                        j -= 1
            direction = turn[direction]
            i -= 1
            j += 1
            if vis_count == nrows * ncols:
                break


            # when going up
            if direction == 'u':
                while(i >= 0):
                    if visited[i][j] == 1:
                        break
                    else:
                        ans.append(matrix[i][j])
                        visited[i][j] = 1
                        vis_count += 1
                        i -= 1
            direction = turn[direction]
            j += 1
            i += 1
            if vis_count == nrows * ncols:
                break

        return ans        