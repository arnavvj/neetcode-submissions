class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:

        # construct graph
        graph = {}
        for [c2, c1] in prereq:
            try:
                graph[c1].add(c2)
            except KeyError:
                graph[c1] = {c2}

        self.graph = graph

        def dfs(c):
            # cycle detected
            if c in self.visited:
                return False

            self.visited.add(c)

            for next_c in self.graph.get(c, []):
                if not dfs(next_c):
                    return False

            self.visited.remove(c)
            return True

        for course in range(numCourses):
            self.visited = set()

            if not dfs(course):
                return False

        return True