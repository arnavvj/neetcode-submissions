# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

""" 
# MY ORIGINAL SOLUTION:
class Codec:
    def preOrder(self, node) -> None:
        if node == None:
            return
        else:
            self.prs += f",{node.val}"
            if node.left != None:
                self.preOrder(node.left)
            if node.right != None:
                self.preOrder(node.right)

    def inOrder(self, node) -> None:

        if not node:
            return
        
        if node.left != None:
            self.inOrder(node.left)
        
        #if node != None:
        self.ios += f",{node.val}"
        
        if node.right != None:
                self.inOrder(node.right)


    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        self.prs = "" # preorder string
        self.preOrder(root)

        self.ios = "" # inorder string
        self.inOrder(root)

        print(self.prs[1:] + '||' + self.ios[1:]) 
        return self.prs[1:] + '||' + self.ios[1:]

    def recreateTree(self, preorder, inorder):
        try:
            root = TreeNode(int(preorder[0]))

            i = 0
            while(i < len(inorder)):
                if preorder[0] == inorder[i]:
                    break
                i += 1

            root.left = self.recreateTree(preorder[1:i+1], inorder[0:i])
            root.right = self.recreateTree(preorder[i+1:], inorder[i+1:])

            return root
        
        except IndexError, ValueError:
            return None

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        [prs, ios] = data.split('||')

        preorder, inorder = prs.split(','), ios.split(',')
        print(preorder)
        print(inorder)
        
        root = self.recreateTree(preorder, inorder)
        return root

        return None


# ==================== WHY THIS APPROACH FAILS ====================

# This implementation uses:
#     - preorder traversal
#     - inorder traversal
# to serialize and reconstruct the tree.

# However, it breaks due to two fundamental issues:

# ------------------------------------------------------------
# 1) MISSING NULL MARKERS → STRUCTURE IS LOST
# ------------------------------------------------------------

# In both traversals:

#     if node == None:
#         return

# You completely skip None nodes.

# This causes different trees to produce the SAME traversal.

# Example:

#     Tree A:        Tree B:
#         1              1
#        /                \
#       2                  2

# Both produce:
#     preorder = [1,2]
#     inorder  = [2,1] or [1,2] depending on shape

# There is no way to distinguish them after serialization.

# 👉 Conclusion:
# Without recording nulls, tree structure is NOT preserved.


# ------------------------------------------------------------
# 2) PREORDER + INORDER FAILS WITH DUPLICATES
# ------------------------------------------------------------

# This method assumes node values are unique.

# Failing test case:
#     root = [3,2,4,3]

# Serialized as:
#     preorder = [3,2,3,4]
#     inorder  = [3,2,3,4]

# Now in reconstruction:

#     if preorder[0] == inorder[i]:

# There are TWO matches for '3' in inorder:
#     index 0 and index 2

# Your code picks the FIRST one:
#     i = 0

# But this may be incorrect.

# 👉 Result:
# Wrong tree structure gets built.

# 👉 Key idea:
# Preorder + Inorder ONLY works if values are UNIQUE.


# ------------------------------------------------------------
# 3) FIRST-MATCH SPLIT IS INCORRECT
# ------------------------------------------------------------

# This loop:

#     while(i < len(inorder)):
#         if preorder[0] == inorder[i]:
#             break

# Always picks the first occurrence.

# With duplicates:
#     inorder = [3,2,3,4]

# You always split at index 0, even if the correct split is index 2.

# This leads to incorrect subtree boundaries.


# ------------------------------------------------------------
# 4) WRONG SUBTREE RECURSION PROPAGATES ERRORS
# ------------------------------------------------------------

# These lines:

#     root.left = self.recreateTree(preorder[1:i+1], inorder[0:i])
#     root.right = self.recreateTree(preorder[i+1:], inorder[i+1:])

# Depend entirely on correct index `i`.

# If `i` is wrong:
#     → left subtree is wrong
#     → right subtree is wrong
#     → entire tree is wrong

# Example wrong output:
#     [3,null,2,null,3,null,4]

# Expected:
#     [3,2,4,3]


# ------------------------------------------------------------
# 5) INVALID PYTHON EXCEPTION SYNTAX
# ------------------------------------------------------------

# This line:

#     except IndexError, ValueError:

# is invalid in Python 3.

# Correct form:

#     except (IndexError, ValueError):

# Also:
# Using exceptions here hides real bugs instead of fixing them.


# ------------------------------------------------------------
# 6) DEAD CODE
# ------------------------------------------------------------

# At the end of deserialize:

#     return root
#     return None   # never executes

# The second return is unreachable.


# ------------------------------------------------------------
# 7) CORE DESIGN PROBLEM
# ------------------------------------------------------------

# This solution assumes:

#     1. Tree can be reconstructed from preorder + inorder
#     2. Structure is implied without nulls

# Both assumptions are FALSE unless:
#     - values are unique
#     - or null markers are stored

# ------------------------------------------------------------
# FINAL TAKEAWAY
# ------------------------------------------------------------

# To correctly serialize/deserialize a binary tree, you need:

# EITHER:
#     - Unique values + traversal combinations

# OR (preferred):
#     - Explicit null markers (e.g., "N") in traversal

# That is why the correct approach uses:

#     preorder traversal + null markers

# Example:
#     1,2,N,N,3,4,N,N,5,N,N

# This preserves:
#     ✔ structure
#     ✔ duplicates
#     ✔ all edge cases

# ============================================================
"""
