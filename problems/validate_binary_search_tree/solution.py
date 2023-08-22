# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     self.CheckBST(root, float("-inf"), float("+inf"))

    # def CheckBST(self, node, left, right):
    #     if not node:
    #         return True

    #     if not(left < node.val < right):
    #         return False

    #     return (self.CheckBST(node.left, left, node.val) and self.CheckBST(node.right, node.val, right))


   def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def CheckBST(node, left, right):
            if not node:
                return True

            if not(left < node.val < right):
                return False

            return (CheckBST(node.left, left, node.val) and CheckBST(node.right, node.val, right))

        return CheckBST(root, float("-inf"), float("+inf"))