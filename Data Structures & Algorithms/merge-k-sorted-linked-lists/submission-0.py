# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge2Lists(self, list1, list2):

        head = ListNode()
        t = head

        n1, n2 = list1, list2
        while(n1 != None and n2 != None):
            
            if n1.val <= n2.val:
                t.next = n1
                n1 = n1.next
            else:
                t.next = n2
                n2 = n2.next

            t = t.next
        
        if n1 != None and n2 == None:
            t.next = n1
        elif n1 == None and n2 != None:
            t.next = n2

        return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        list1, list2 = None, None
        try:
            while(len(lists) > 1):
                list1 = lists.pop(0)
                list2 = lists.pop(0)
                mlist = self.merge2Lists(list1, list2)
                lists = [mlist] + lists

            return lists[0]

        except IndexError:
            if list1 == None:
                return None
            else:
                return list1

