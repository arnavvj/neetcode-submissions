# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        if head.next == None:
            return head

        back = head
        frnt = head.next
        back.next = None

        while (frnt != None):

            frnt_frnt = frnt.next
            frnt.next = back

            back = frnt
            frnt = frnt_frnt

        return back



"""

    2 -> None
            h
            2 <- 3 <- 4 <- 5    None
back                       ^
frnt                             ^
frnt_frnt                        ^


"""