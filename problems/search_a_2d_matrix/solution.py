class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nrow = len(matrix)
        ncol = len(matrix[0])
        start = 0
        end = nrow -1

        row_index = self.rowBinarySearch(matrix, start, end, target, ncol-1)
        if row_index == -1:
            return False
        
        col_index = self.colBinarySearch(matrix[row_index], 0, ncol-1, target)
        if col_index == -1:
            return False
        
        return True

    def colBinarySearch(self,nums, start, end, target):
        if start > end:
            return -1
        
        mid = int((start + end)/2)
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.colBinarySearch(nums, start, mid-1, target)
        else:
            return self.colBinarySearch(nums, mid+1, end, target)
    
    def rowBinarySearch(self, nums, start, end, target,ncol):
        if start > end:
            return -1

        mid = int((start + end)/2)
        if nums[mid][0] <= target and target <= nums[mid][ncol]:
            return mid

        elif target < nums[mid][0]:
            return self.rowBinarySearch(nums, start, mid-1,target,ncol)
        else:
            return self.rowBinarySearch(nums, mid+1, end, target, ncol)