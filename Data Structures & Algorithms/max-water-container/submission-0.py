class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = float("-inf")

        while l < r:
            length = min(heights[l], heights[r])
            breadth = abs(l - r)

            max_area = max(max_area, (length * breadth))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area