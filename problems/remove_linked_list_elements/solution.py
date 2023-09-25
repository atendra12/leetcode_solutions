# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        pt = dummy

        while pt and pt.next:
            if pt.next.val == val:
                pt.next = pt.next.next
            else:
                pt = pt.next

        return dummy.next

