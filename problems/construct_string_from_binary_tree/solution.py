# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            tempStr = ''
            if not root:
                return None

            tempStr = str(root.val)
            left = helper(root.left)
            right = helper(root.right)

            if not left and right:
                tempStr += '()'
                tempStr += right
            
            if left and not right:
                tempStr += left
            
            if left and right:
                tempStr += left + right
            
            return '(' + tempStr + ')'

        return helper(root)[1:-1]