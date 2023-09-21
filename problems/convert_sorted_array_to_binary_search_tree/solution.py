# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        res = []
        left, right = 0, len(nums) -1

        def BST(left, right):
            if left > right:
                return None
            
            middle = (right + left) // 2
            root = TreeNode(nums[middle])
            root.left = BST(left, middle -1)
            root.right = BST(middle+1, right)
        
            return root
        
        return BST(left, right)


        