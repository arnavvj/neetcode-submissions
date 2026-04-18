"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def bfs(self, node, clone_node):

        self.visited.add(node)

        if node.neighbors:
            clone_node.neighbors = []

            for n in node.neighbors:
                try:
                    clone_node.neighbors.append( self.cloneNodeMap[n] )

                except KeyError:
                    self.cloneNodeMap[n] = Node(n.val)
                    clone_node.neighbors.append( self.cloneNodeMap[n] )

            for n, cn in zip(node.neighbors, clone_node.neighbors):
                if n not in self.visited:
                    self.bfs(n , cn)


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None:
            return None

        self.cloneNodeMap, self.visited = dict(), set()
        self.cloneNodeMap[node] = Node(node.val)
        self.visited.add(node)
        clone_node = self.cloneNodeMap[node]
        
        if node.neighbors:
            clone_node.neighbors = []

            for n in node.neighbors:
                try:
                    clone_node.neighbors.append( self.cloneNodeMap[n] )

                except KeyError:
                    self.cloneNodeMap[n] = Node(n.val)
                    clone_node.neighbors.append( self.cloneNodeMap[n] )
                    
                for n, cn in zip(node.neighbors, clone_node.neighbors):
                    if n not in self.visited:
                        self.bfs(n , cn)

        return clone_node
        