# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## Base logic
        if root == None:
            return root

        new_left = self.invertTree(root.left)
        new_right = self.invertTree(root.right)

        root.left, root.right = new_right, new_left
        return root
        




