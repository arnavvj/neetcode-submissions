# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        try:

            if type(preorder) != list:
                return None
            
            if len(preorder) == 0:
                return None

            else:
                root = TreeNode(preorder[0])

                # locate pivot
                j = 0
                while (j < len(inorder)):
                    if preorder[0] == inorder[j]:
                        break
                    j+=1

                root.left = self.buildTree(
                    preorder[1:j+1], 
                    inorder[:j]
                )
                
                root.right = self.buildTree(
                    preorder[j+1:], 
                    inorder[j+1:]
                )

        except KeyError:
            return None


        return root


"""
            1
          /   \
         2     3
        / \     \
       6  5      4
           \
            7

         0  1  2  3  4  5  6
    pre: 1  2  6  5  7  3  4
         ^  ----------  ----

         ----------  v  ----  
    in:  6  2  5  7  1  3  4
         0  1  2  3  4  5  6
"""
        