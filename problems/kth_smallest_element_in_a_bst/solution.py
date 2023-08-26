# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global result
        result = []

        def inorder_traverse(root):
            global result

            if not root:
                return 

            inorder_traverse(root.left)
            result.append(root.val)
            inorder_traverse(root.right)
        
        inorder_traverse(root)
        return result[k-1]



