#using binary search on rows when top is equal to bottom move on to checking the columns within the row
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) -1

        while t <= b:
            row = t + (b-t) //2
            if matrix[row][-1] < target:
                t = row + 1
            elif matrix[row][0] > target:
                b = row - 1
            else:
                break

        if t > b:
            return False

        l = 0
        r = len(matrix[row]) -1
        while l <= r:
            m = l + (r - l) //2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
