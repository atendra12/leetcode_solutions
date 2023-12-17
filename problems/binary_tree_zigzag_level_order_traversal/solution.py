# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        from collections import deque 
        
        results = []
        
        queue = deque()
        queue.append([root])
        
        while(len(queue) > 0):
            
            ## level address
            node_list = queue.popleft()
            
            result = []
            node_add = []
            
            for node in node_list:
                result.append(node.val)
                
                if node.left is not None:
                    node_add.append(node.left)
                if node.right is not None:
                    node_add.append(node.right)
                    
            if len(result)> 0:
                results.append(result)
            if len(node_add)> 0:
                queue.append(node_add)
        for index in range(len(results)):
            if(index%2 != 0):
                results[index].reverse()
        return results
                
        
                
                    
                 
        
        
        
        
  
        
            
        

        