import copy


class Solution:

    def dfs(self, board, word, i, j) -> bool:
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] == None:
            return False

        if word[0] == board[i][j]:
            if len(word) == 1:
                return True
            else:
                board_ = copy.deepcopy(board)
                board_[i][j] = None
                if self.dfs(board_, word[1:], i+1, j):
                    print("d")
                    return True
                if self.dfs(board_, word[1:], i-1, j):
                    print("u")
                    return True
                if self.dfs(board_, word[1:], i, j+1):
                    print("r")
                    return True
                if self.dfs(board_, word[1:], i, j-1):
                    print("l")
                    return True

        ans = False


        


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if len(word) == 1:
                        return True
                    else:
                        board_ = copy.deepcopy(board)
                        board_[i][j] = None
                        if self.dfs(board_, word[1:], i+1, j):
                            print("d")
                            return True
                        if self.dfs(board_, word[1:], i-1, j):
                            print("u")
                            return True
                        if self.dfs(board_, word[1:], i, j+1):
                            print("r")
                            return True
                        if self.dfs(board_, word[1:], i, j-1):
                            print("l")
                            return True

        return False


        