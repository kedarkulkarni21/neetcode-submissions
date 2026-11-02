class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        j = len(nums)

        while i < j:
            if nums[i] == val:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        return i
