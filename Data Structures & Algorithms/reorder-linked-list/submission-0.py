# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        temp, head.prev = head, None
        while(temp.next != None):
            temp.next.prev = temp
            temp = temp.next

        last = temp
        first = head

        while (first != last and first.next != last):

            first_next = first.next
            last_prev = last.prev

            first.next = last
            last_prev.next  = last.next
            last.next = first_next

            first = first_next
            last = last_prev