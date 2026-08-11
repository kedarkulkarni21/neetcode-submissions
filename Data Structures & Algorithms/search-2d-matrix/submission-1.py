class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total_nums = rows * cols
        left = 0
        right = total_nums - 1

        while left <= right:
            mid_point = (left + right) // 2
            i = mid_point // cols
            j = mid_point % cols
            middle_num = matrix[i][j]

            if target == middle_num:
                return True
            
            if target < middle_num:
                right = mid_point - 1
            else:
                left = mid_point + 1

        return False