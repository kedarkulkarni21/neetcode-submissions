class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)

        # True if no cycle, False if cycle
        def dfs(i):
            if states[i] == VISITING:
                return False

            if states[i] == VISITED:
                return True

            states[i] = VISITING
            for nei in graph[i]:
                if not dfs(nei):
                    return False

            states[i] = VISITED
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order