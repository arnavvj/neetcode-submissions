# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        tail = head
        for i in range(0, n):
            tail = tail.next

        if tail == None:
            return head.next

        front = head

        while(tail.next != None):
            tail, front = tail.next, front.next

        front.next = front.next.next

        return head