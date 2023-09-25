# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## reverse linked list from slow
        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow 
            slow = temp
        
        pt1, pt2 = head, prev

        while pt2:            
            if pt1.val != pt2.val:
                return False
            
            pt1 = pt1.next
            pt2 = pt2.next
            
        return True




        

        