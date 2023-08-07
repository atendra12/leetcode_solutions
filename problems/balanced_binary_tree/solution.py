# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global flag
        flag = True

        def dfs(root):
            global flag
            if not root:
                return -1
        
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) > 1:
                    flag = False

            height = max(left,right) + 1

            return height
        dfs(root)
        return flag
