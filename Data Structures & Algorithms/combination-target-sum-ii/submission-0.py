class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, sol, curr_total):
            if curr_total == target:
                res.append(sol.copy())
                return

            if i >= len(candidates) or curr_total > target:
                return

            sol.append(candidates[i])
            dfs(i + 1, sol, curr_total + candidates[i])
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, sol, curr_total)

        dfs(0, [], 0)

        return res