from typing import List

class Node:
    def __init__(self):
        self.kids = {}
        self.word = None


class Solution:

    def buildTrie(self, words):
        root = Node()

        for word in words:
            curr = root

            for ch in word:
                if ch not in curr.kids:
                    curr.kids[ch] = Node()

                curr = curr.kids[ch]

            curr.word = word

        return root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = self.buildTrie(words)

        rows = len(board)
        cols = len(board[0])

        ans = []

        def dfs(r, c, node):

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols
            ):
                return

            ch = board[r][c]

            if ch == '#' or ch not in node.kids:
                return

            nxt = node.kids[ch]

            if nxt.word is not None:
                ans.append(nxt.word)
                nxt.word = None      # prevent duplicates

            board[r][c] = '#'

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return ans