# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        elif root.left.val == root.right.val:
            l = TreeNode(val=root.left.val, left=root.left.left, right=root.right.right)
            r = TreeNode(val=root.right.val, left=root.right.left, right=root.left.right)
            if self.isSymmetric(l) and self.isSymmetric(r):
                return True
            else:
                return False
        else:
            return False
