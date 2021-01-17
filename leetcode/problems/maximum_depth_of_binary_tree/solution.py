# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #leaf node -- both childs are null
        ## farthest leaf
        ## max(left,right)
        if(root ==None):
            return 0
        if(root.left == None and root.right ==None):
            return 1
        left = root.left
        right = root.right
        #print(left)
        #print(right)
        left_height = 1 + self.maxDepth(left)
        right_height = 1 + self.maxDepth(right)
        return max(left_height,right_height)
        
    
        
        