# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def recTravel(self, node: Optional[TreeNode]) -> int:
        
        if node.left == None and node.right == None:
            return 1

        else:
            lt_ht, rt_ht = 0, 0

            if node.left != None:
                lt_ht = self.recTravel(node.left)

            if node.right != None:
                rt_ht = self.recTravel(node.right)

            return max(lt_ht, rt_ht) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        else:
            lt_ht, rt_ht = 0, 0

            if root.left != None:
                lt_ht = self.recTravel(root.left)

            if root.right != None:
                rt_ht = self.recTravel(root.right)

            return max(lt_ht, rt_ht) + 1

