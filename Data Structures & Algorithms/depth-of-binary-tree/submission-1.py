# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        elif root.left == None and root.right == None:
            return 1

        else:
            lt_ht, rt_ht = 0, 0

            if root.left != None:
                lt_ht = self.maxDepth(root.left)

            if root.right != None:
                rt_ht = self.maxDepth(root.right)

            return max(lt_ht, rt_ht) + 1

