# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        level_info = collections.deque()
        level_info.append(root)

        while level_info:
            level_order = []
            length = len(level_info)
            for i in range(length):
                node = level_info.popleft()
                if node:
                    level_info.append(node.left)
                    level_info.append(node.right)
                    level_order.append(node.val)
                
            if level_order:
                result.append(level_order[-1])
        return result


        # result = []
        # cur = root
        # while cur:
        #     result.append(cur.val)
        #     cur = cur.right
        # return result
            