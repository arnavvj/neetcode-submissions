# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = list()
        
        if root == None:
            return root
        else:
            queue.append(root)

        while len(queue) > 0:

            node = queue.pop(0)

            # swap
            node_l = node.left
            node.left = node.right
            node.right = node_l

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        
        return root
        
        