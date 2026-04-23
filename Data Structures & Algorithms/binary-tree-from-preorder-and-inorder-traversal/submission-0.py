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

                j = 0
                while (j < len(inorder)):
                    if preorder[0] == inorder[j]:
                        break
                    j+=1

                root.left = self.buildTree(preorder[1:j+1], inorder[:j])
                root.right = self.buildTree(preorder[j+1:], inorder[j+1:])

        except KeyError:
            return None


        return root
        