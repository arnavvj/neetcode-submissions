# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    ans = float('-inf')

    def pathSum(self, node):

        if node.left == None and node.right == None:
            self.ans = max(self.ans, node.val)
            return node.val

        left_max_path_sum, right_max_path_sum = 0, 0
        if node.left != None:
            left_max_path_sum = self.pathSum(node.left)
        if node.right != None:
            right_max_path_sum = self.pathSum(node.right)
        
        self.ans = max(    
            self.ans,
            node.val,
            node.val + left_max_path_sum,
            node.val + right_max_path_sum,
            node.val + left_max_path_sum + right_max_path_sum
        )

        return max(
            node.val,
            node.val + left_max_path_sum,
            node.val + right_max_path_sum
        )


    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        left_max_path_sum, right_max_path_sum = 0, 0
        if root.left != None:
            left_max_path_sum = self.pathSum(root.left)
        
        if root.right != None:
            right_max_path_sum = self.pathSum(root.right)

        self.ans = max(
            
            self.ans,

            root.val, 

            root.val + left_max_path_sum,

            root.val + right_max_path_sum,

            root.val + left_max_path_sum + right_max_path_sum
        )

        return self.ans