# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(pt1, pt2):
            if not pt1 and not pt2:
                return True
            
            if not pt1 or not pt2:
                return False

            return pt1.val == pt2.val and dfs(pt1.left, pt2.right) and dfs(pt1.right, pt2.left)            
        
        return dfs(root.left, root.right)

            


        


        