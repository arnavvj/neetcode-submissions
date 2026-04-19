# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def findNode(self, node, subroot):
        if node.val == subroot.val:
            self.targets.append(node)
        if node.left != None:
            self.findNode(node.left, subroot)
        if node.right != None:
            self.findNode(node.right, subroot)

    def levelCheck(self, node1, node2):
        q1, q2 = [node1], [node2]

        while(len(q1) != 0 and len(q2) != 0):
            node1, node2 = q1.pop(0), q2.pop(0)
            try:
                if node1.val != node2.val:
                    return False
                print(node1.val, node2.val)
                
                if type(node1.left) != type(node2.left):
                    return False
                q1.append(node1.left)
                q2.append(node2.left)

                if type(node1.right) != type(node2.right):
                    return False
                q1.append(node1.right)
                q2.append(node2.right)
            
            except AttributeError:
                print(node1, node2)
                if node1 != node2:
                    return False
        
        print(q1, q2)
        if len(q1) != 0 or len(q2) != 0:
            return False

        return True
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.targets = []
        self.findNode(root, subRoot)
        if len(self.targets) == 0:
            return False

        ans = False
        for t in self.targets:
            ans = ans or self.levelCheck(t, subRoot)

        return ans
        