"""Search 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true
Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Check if the input matrix is empty (i.e., no rows or no columns)
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        
        # Initialize pointers for binary search
        row_start, col_end = 0, rows * cols - 1  
        
        while row_start <= col_end:  
            # Calculate the middle element index
            mid = (row_start + col_end) // 2
            
            # Get the value of the middle element
            mid_val = matrix[mid // cols][mid % cols]  # Mid_val = Matrix[mid_row][mid_col]
            
            # Compare the target to the middle element
            if mid_val == target:  
                return True  # Target found! Return true
            elif mid_val < target:  
                # If the target is greater than the middle element, move col_end pointer to mid + 1
                row_start = mid + 1  
            else:
                # If the target is less than the middle element, move row_start pointer to mid - 1
                col_end = mid - 1
        
        return False  # Target not found in matrix (loop completes without finding target)

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15

# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target = 10

sol = Solution()
print(sol.searchMatrix(matrix, target))
