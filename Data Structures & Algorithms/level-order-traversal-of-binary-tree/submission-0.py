# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        if root == None:
            return ans

        ans.append([root.val])
        
        next_line = []
        if root.left != None:
            next_line.append(root.left)
        if root.right != None:
            next_line.append(root.right)

        while (len(next_line)):

            next_next_line, temp = [], []
            
            for curr in next_line:

                temp.append(curr.val)

                if curr.left != None:
                    next_next_line.append(curr.left)
                if curr.right != None:
                    next_next_line.append(curr.right)

            ans.append(temp)
            next_line = next_next_line

            del(next_next_line, temp)

        return ans
        