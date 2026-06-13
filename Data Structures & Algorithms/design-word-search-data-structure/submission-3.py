class Node:
    def __init__(self):
        self.kids = dict()
        self.term = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr, i = self.root, 0

        while(i<len(word)):
            if word[i] not in curr.kids:
                curr.kids[word[i]] = Node()
            
            curr = curr.kids[word[i]]
            i += 1

        curr.term = True
        

    def search(self, word: str) -> bool:

        def recurSearch(word, nxt) -> bool:
            if word == '':
                return nxt.term
            
            if word[0] in nxt.kids:
                return recurSearch(word[1:], nxt.kids[word[0]])
            elif word[0] == '.':
                ans = False
                for c in nxt.kids:
                    ans = ans or recurSearch(word[1:], nxt.kids[c])
                return ans
            else:
                return False

        curr = self.root
        if word[0] in curr.kids:
            return recurSearch(word[1:], curr.kids[word[0]])
        elif word[0] == '.':
            ans = False
            for c in curr.kids:
                ans = ans or recurSearch(word[1:], curr.kids[c])
            return ans
        else:
            return False
