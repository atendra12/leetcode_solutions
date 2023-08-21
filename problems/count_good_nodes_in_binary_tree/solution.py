# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodeCount(root,root.val)

    def goodNodeCount(self, root, MaxValue):
        count = 0
        if not root:
            return count
        if root.val >= MaxValue:
            count = 1
            MaxValue = root.val

        return count + self.goodNodeCount(root.left,MaxValue) + self.goodNodeCount(root.right,MaxValue)


    

    



