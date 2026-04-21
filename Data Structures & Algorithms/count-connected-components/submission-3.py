class Node:
    def __init__(self):
        self.adj_set = set()
        self.visited = False

class Solution:


    def travel(self, v):
        
        if not self.graph[v].visited:            
            print("inner", v, self.graph[v].visited)
            self.graph[v].visited = True
            print("marked", v, self.graph[v].visited)
            for next_v in self.graph[v].adj_set:
                self.travel(next_v)
            print()


    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.graph = dict()

        for v in range(n):
            self.graph[v] = Node()
        
        for [v1, v2] in edges:
            self.graph[v1].adj_set.add(v2)
            self.graph[v2].adj_set.add(v1)
            

        print("######## GRAPH:")
        for (v, n) in self.graph.items():
            print(v, n.adj_set, n.visited)


        print("\n\n######## EXPLORATION:")
        count = 0
        for v in self.graph.keys():
            print("outer", v, self.graph[v].visited)
            if self.graph[v].visited == False:
                self.travel(v)
                count += 1

        return count
        


"""

self.graph = {

    0 : Node(
        adj_list -> {1}
        visited -> False
    )

}
"""