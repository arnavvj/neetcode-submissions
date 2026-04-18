# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findRoute(self, root_, node_) -> list:
        stack = []
        while (root_.val != node_.val):

            stack.append(root_)

            if node_.val < root_.val:
                root_ = root_.left
            else:
                root_ = root_.right

        stack.append(node_)
        return stack


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root == p or root == q:
            return root

        p_stack = self.findRoute(root, p)
        q_stack = self.findRoute(root, q)

        if len(q_stack) < len(p_stack):
            p_stack, q_stack = q_stack, p_stack

        ans = None
        for i, p_node in enumerate(p_stack):
            
            if p_node.val != q_stack[i].val:
                break

            ans = p_node

        return ans 


