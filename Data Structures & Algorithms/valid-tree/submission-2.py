class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue

                if not dfs(nei, curr):
                    return False
                
            return True

        return dfs(0, -1) and n == len(visited)
