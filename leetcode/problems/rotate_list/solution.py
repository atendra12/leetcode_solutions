# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        current = head
        count = 0
        while current is not None:
            current = current.next
            count +=  1
            
        k = k%count
        
        iter_count = count - k
        current = head
        
        for i in range(iter_count-1):
            current = current.next
            
        new_head= current.next
        new_pt = current.next
        
        if new_pt is None:
            return head
        
        current.next = None
        while new_pt.next is not None:
            new_pt = new_pt.next
            
        new_pt.next = head
        return new_head
            
        
        