class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, sol, curr_total):
            if curr_total == target:
                res.append(sol[:])
                return

            if i >= len(nums) or curr_total > target:
                return

            # pick nums[i]
            sol.append(nums[i])
            dfs(i, sol, curr_total + nums[i])
            sol.pop()

            # don't pick nums[i]
            dfs(i + 1, sol, curr_total)

        dfs(0, [], 0)
    
        return res

        
