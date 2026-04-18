# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], low = float('-inf'), high = float('inf')) -> bool:
        print(low, root.val, high)
        if low >= root.val or root.val >= high:
            return False 

        ans = True

        if root.left != None:
            if root.left.val >= root.val:
                return False
            else:
                ans = ans and self.isValidBST(root.left, low, root.val)

        if ans == False:
            return ans

        if root.right != None:
            if root.right.val <= root.val:
                return False
            else:
                ans = ans and self.isValidBST(root.right, root.val, high)

        return ans