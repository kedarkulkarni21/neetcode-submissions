class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = set()
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(curr):
            for nei in adj[curr]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

            return

        for node in range(n):
            if node not in visited:
                visited.add(node)
                components += 1
                dfs(node)

        return components
