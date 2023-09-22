# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # if not root and targetSum ==0:
        #     return False

        # def helper(root, targetSum):
        #     # if targetSum < 0:
        #     #     return False
            
        #     # if not root and targetSum > 0:
        #     #     return False
            
        #     # if not root:
        #     #     return True

        #     # if root.val == targetSum:
        #     #     return True
            
        #     ## Base Case
        #     if targetSum < 0:
        #         return False

        #     if not root and targetSum > 0:
        #         return False
            
        #     if not root and targetSum == 0:
        #         return True
                
        #     return helper(root.left, targetSum - root.val) or helper(root.right, targetSum - root.val)
        
        # return helper(root, targetSum)

        if not root:
            return False
        
        if root.val == targetSum and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)   

            
            