# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p == None and q == None:
            return True
        elif p == None and q != None or p != None and q == None:
            return False

        if p.val != q.val:
            return False
        
        qu_p, qu_q = [p], [q]

        while(len(qu_p) == len(qu_q) and len(qu_p) != 0 and len(qu_q) != 0):

            p_ = qu_p.pop(0)
            p_l, p_r = p_.left, p_.right

            q_ = qu_q.pop(0)
            q_l, q_r = q_.left, q_.right


            # LEFT CHECK
            if p_l != None and q_l != None:
                if p_l.val != q_l.val:
                    return False
                else:
                    qu_p.append(p_l)
                    qu_q.append(q_l)
            elif p_l == None and q_l == None:
                pass
            else:
                return False


            # RIGHT CHECK
            if p_r != None and q_r != None:
                if p_r.val != q_r.val:
                    return False
                else:
                    qu_p.append(p_r)
                    qu_q.append(q_r)
            elif p_r == None and q_r == None:
                pass
            else:
                return False


        if len(qu_p) != len(qu_q):
            return False

        return True
