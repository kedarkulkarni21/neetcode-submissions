class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()

        for num in nums:
            if num not in hset:
                hset.add(num)
            else:
                return True

        return False
        