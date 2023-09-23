# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
            
        # minval = float('inf')
        # if root.left:
        #     minval = min(minval, root.val - root.left.val, self.minDiffInBST(root.left))

        # if root.right:
        #     minval = min(minval, root.right.val - root.val, self.minDiffInBST(root.right))
            
        # return minval

        ## Logic: BST -- sorted -- inorder traversal -- two pointer approach

        prev, res = None, float('inf')

        def dfs(root):
            nonlocal prev, res
            if not root:
                return
            
            dfs(root.left)
            if prev:
                res = min(res, root.val - prev.val)
            prev = root
            dfs(root.right)
        
        dfs(root)
        return res






