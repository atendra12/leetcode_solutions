# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        first = head
        second = head.next

        while second and second.next:
            first = first.next
            second = second.next.next
        
        second = first.next
        first.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, last = head, prev
        while last:
            temp1 = first.next
            temp2 = last.next
            first.next = last
            last.next = temp1
            first = temp1
            last = temp2
        



        

        

        

        





        









        








