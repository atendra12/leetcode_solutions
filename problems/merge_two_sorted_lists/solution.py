# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        newHead = None

        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val >= curr2.val:
                    new_entry = ListNode(curr2.val)
                    curr2 = curr2.next
                else:
                    new_entry = ListNode(curr1.val)
                    curr1 = curr1.next
            else:
                if curr1:
                    new_entry = ListNode(curr1.val)
                    curr1 = curr1.next
                if curr2:
                    new_entry = ListNode(curr2.val)
                    curr2 = curr2.next

            if newHead:
                curr3.next = new_entry
                curr3 = curr3.next
            else:
                newHead = new_entry
                curr3 = newHead
        
        return newHead
            






        














        





