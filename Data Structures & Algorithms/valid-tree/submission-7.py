class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case
        if not edges:
            return True
        
        # first check if theres a loop
        visited, graph = set(), {}
        for [v1, v2] in edges:
            if v1 == v2:
                return False
            # elif v1 in visited and v2 in visited:
            #     return False
            else:
                try:
                    visited.add(v1)
                    graph[v1].add(v2)
                except KeyError:
                    graph[v1] = {v2}
                try:
                    visited.add(v2)
                    graph[v2].add(v1)
                except KeyError:
                    graph[v2] = {v1}



        # can you traverse all nodes starting from any node
        q = [visited.pop()]
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

        
        return True if count == n else False
        




        