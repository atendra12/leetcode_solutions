# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_dim
        max_dim = 0
        def diameterheightofBT(root):
            global max_dim
            if not root:
                return -1

            left_height = diameterheightofBT(root.left)
            right_height = diameterheightofBT(root.right)

            height_node = max(left_height,right_height) + 1
            dim = left_height + right_height + 2

            max_dim = max(max_dim, dim)
            return height_node
        
        diameterheightofBT(root)
        return max_dim
    





        


        






