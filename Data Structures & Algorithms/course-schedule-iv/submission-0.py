class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        pre_req = {}
        res = []

        for u, v in prerequisites:
            adj[v].append(u)

        def dfs(crs):
            if crs not in pre_req:
                pre_req[crs] = set()
                for pre in adj[crs]:
                    pre_req[crs] = pre_req[crs] | dfs(pre)

                pre_req[crs].add(crs)

            return pre_req[crs]

        for course in range(numCourses):
            dfs(course)

        for u, v in queries:
            res.append(u in pre_req[v])

        return res