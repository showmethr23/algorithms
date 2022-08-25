# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val = 0, left = None, right = None)
#       self.val = val
#       self.left = left
#       self.right = right

# Valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key
# The right subtree of a node contains only nodes with keys greater than the node's key
# Both the left and right subtrees must also be binary search trees

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Solution 1
        

