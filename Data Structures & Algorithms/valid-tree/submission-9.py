class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case
        if not edges:
            return True
        
        # make adjacency set graph structure
        # eliminate possibility of same node loop in [v1 <-> v1]
        graph = {}
        for [v1, v2] in edges:
            if v1 == v2:
                return False
            else:
                try:
                    graph[v1].add(v2)
                except KeyError:
                    graph[v1] = {v2}
                try:
                    graph[v2].add(v1)
                except KeyError:
                    graph[v2] = {v1}


        # can you traverse all nodes starting from any node 
        # loop check is there to avoid infinite recursive search
        q = [
            [*graph.keys()][0]
        ]
        visited, count = set(), 0

        while(len(q) != 0):
            start = q.pop(0)
            visited.add(start)
            count += 1

            for v in graph[start]:
                if v in visited:
                    continue
                else:
                    q.append(v)


        if count == n:
            return True  
        else:
            return False
        




        