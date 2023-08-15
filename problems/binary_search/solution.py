class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        return self.binarySearchTree(nums, start, end, target)
    
    def binarySearchTree(self, nums, start, end, target):
        ## Base Case
        if start > end:
            return -1
        
        ## Middle point
        mid = int((start + end)/2)

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            ## search in left tree
            return self.binarySearchTree(nums, start, mid-1, target)
        else:
            ## search in right tree
            return self.binarySearchTree(nums, mid+1, end, target)

            



