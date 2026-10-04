class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,btn = 0, len(matrix) - 1

        while top <= btn:
            row = (top + btn) // 2

            if target < matrix[row][0]:
                btn = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

            
        if not (top <= btn):
            return False

        row = (top + btn) // 2
        l,r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l+r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else: 
                l = m + 1

        return False