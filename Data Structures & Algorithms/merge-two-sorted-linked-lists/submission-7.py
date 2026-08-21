# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(None)
        
        p, p1, p2 = head, list1, list2

        while (p1 != None and p2 != None):

            if p1.val <= p2.val:
                p.next = p1
                p, p1 = p.next, p1.next

            else:
                p.next = p2
                p, p2 = p.next, p2.next


        if p1 != None:
            p.next = p1
        elif p2 != None:
            p.next = p2

        return head.next