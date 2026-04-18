# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inordTrav(self, node, k, counter):

        if node.left != None:
            node_, counter = self.inordTrav(node.left, k, counter)
            if counter == k:
                return node_, counter

        counter += 1
        if counter == k:
            return node, counter

        if node.right != None:
            node_, counter = self.inordTrav(node.right, k, counter)
            if counter == k:
                return node_, counter

        return node, counter


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        found, counter = self.inordTrav(root, k, counter)
        return found.val if k == counter else None
        