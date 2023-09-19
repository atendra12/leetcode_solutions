# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## pre order
        ## root, left, right

        ## In order
        ## left, root, right

        ## post order
        ### left right root

        result = []

        def trav(root):
          if not root:
              return
          
          trav(root.left)
          result.append(root.val)
          trav(root.right)

        trav(root)

        return result


        