# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
                    
        result = []
        dq = deque([root])

        while dq:
            level_order = []
            for index in range(len(dq)):
                node = dq.popleft()
                if not node:
                    continue
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)           
                level_order.append(node.val)
            result.append(level_order)
        return result



