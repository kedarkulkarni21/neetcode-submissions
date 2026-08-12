class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            
            if state == VISITING:
                return False

            states[node] = VISITING
            for course in graph[node]:
                if not dfs(course):
                    return False
            
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True