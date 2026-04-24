# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # --------------------------------
        def inOrder(node):
            if not node:
                self.ios += ',#'
                return

            self.ios += f',{node.val}'
            inOrder(node.left)
            inOrder(node.right)
        # --------------------------------

        self.ios = ""
        inOrder(root)
        print(f"serialized inOrder: {self.ios[1:]}")
        return self.ios[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        # --------------------------------
        def revInOrder():
            try:
                val = self.iq.pop(0)
                
                if val == '#':
                    return None

                root = TreeNode(int(val))
                root.left = revInOrder()
                root.right = revInOrder()

                return root
             
            except IndexError:
                return None
        # --------------------------------

        self.iq = data.split(',')
        return revInOrder()
