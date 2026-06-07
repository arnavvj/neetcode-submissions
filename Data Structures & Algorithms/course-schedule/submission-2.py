class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:

        # construct graph and note independent courses
        graph, indie = {}, {}
        for [c2, c1] in prereq:
            try:
                graph[c1].add(c2)
            except KeyError:
                graph[c1] = {c2}

            indie[c1] = indie.get(c1, True) and True
            indie[c2] = indie.get(c2, False) and False

        def dfs(c):

            if c in self.visited:
                return False

            self.visited.add(c)

            next_l = self.graph.get(c, [])
            for next_c in next_l:
                if not dfs(next_c):
                    return False

            self.visited.remove(c)
            return True

        self.graph = graph

        for i in range(numCourses):
            self.visited = set()

            if not dfs(i):
                return False

        return True