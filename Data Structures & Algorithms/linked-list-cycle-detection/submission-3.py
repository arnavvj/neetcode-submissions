# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False
        
        head.visited = False
        
        while(head != None):
            try:
                if head.visited == True:
                    return True

                else:
                    head.visited = True
                    head = head.next

            except AttributeError:
                
                head.visited = True
                head = head.next

        return False

