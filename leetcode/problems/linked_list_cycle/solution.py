# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        slow = head
        fast = head.next
        """
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        """
        while slow!=None:
            if fast == None or fast.next == None:
                return False
            else:
                if(slow==fast):
                    return True
                slow = slow.next
                fast = fast.next.next
        
                
            
            
            
            
        
        
        
        
        