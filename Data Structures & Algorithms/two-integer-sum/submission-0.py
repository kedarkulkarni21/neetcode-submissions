class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find not in hmap:
                hmap[num] = i
            else:
                return [hmap[to_find], i]