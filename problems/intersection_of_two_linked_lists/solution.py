# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0

        first, second = headA, headB

        while first:
            lenA +=1
            first = first.next

        while second:
            lenB +=1
            second = second.next

        first, second = headA, headB

        if lenA > lenB:
            diff = lenA - lenB
            ## MOVE A
            while diff > 0:
                first = first.next
                diff -=1
        else:
            diff = lenB - lenA
            while diff > 0:
                second = second.next
                diff -=1
        
        while first and second:
            if first == second:
                return first

            first = first.next
            second = second.next
            
        return None






    
        

        