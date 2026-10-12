class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_mult = 1
        right_mult = 1
        res = [1] * n

        for i in range(n):
            res[i] = left_mult
            left_mult *= nums[i]            

        for j in range(n - 1, -1, -1):
            res[j] *= right_mult
            right_mult *= nums[j]            

        return res
