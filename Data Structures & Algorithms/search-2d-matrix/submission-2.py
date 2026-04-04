class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start = 0

        row = len(matrix)
        column = len(matrix[0])
        end = row*column-1

        while start <= end:

            mid = (start + end) //2

            r, c = mid//column, mid%column

            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                start = mid +1
            else:
                end = mid - 1
        return False
        


