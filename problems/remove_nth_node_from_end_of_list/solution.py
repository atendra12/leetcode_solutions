# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) ## by adding dummy node you have shifted LL size for N+1
        slow = dummy
        fast = head

        while n > 0 and fast:
            fast = fast.next
            n -=1

        while fast:
            fast = fast.next
            slow = slow.next
    
        ## slow.next need to be delete
        slow.next = slow.next.next
    
        return dummy.next




        