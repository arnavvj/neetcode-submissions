class Node:

    def __init__(self):
        self.kids = {}



class PrefixTree:

    def __init__(self):
        self.root = Node()
        self.root.term = False
        self.root.char = None


    def insert(self, word: str) -> None:

        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.kids.keys():
                curr.kids[word[i]] = Node()

                curr.kids[word[i]].char = word[i]
                curr.kids[word[i]].term = False
            
            curr = curr.kids[word[i]]

        curr.term = True


    def search(self, word: str) -> bool:

        curr = self.root

        for i in range(len(word)):
            if word[i] in curr.kids.keys():
                curr = curr.kids[word[i]]
                if word[i] != curr.char:
                    return False

            else:
                return False

        return curr.term

        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for i in range(len(prefix)):
            if prefix[i] in curr.kids.keys():
                curr = curr.kids[prefix[i]]
                if prefix[i] != curr.char:
                    return False

            else:
                return False

        return True 
        
        