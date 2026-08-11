class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        l = 0
        r = total - 1

        while l <= r:
            mid = (l + r) // 2
            i = mid // cols
            j = mid % cols
            mid_num = matrix[i][j]

            if target == mid_num:
                return True

            if target < mid_num:
                r = mid - 1
            else:
                l = mid + 1

        return False