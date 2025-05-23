# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree.
        The LCA is the lowest node that has both p and q as descendants (a node can be a descendant of itself).

        Args:
            root (TreeNode): The root of the BST.
            p (TreeNode): First target node.
            q (TreeNode): Second target node.

        Returns:
            TreeNode: The LCA node.
        """
        while root:
            # If both nodes p and q are smaller than root, LCA is in left subtree.
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both nodes p and q are greater than root, LCA is in right subtree.
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # We have found the split point where p and q lie in different subtrees
                # or one is equal to root, so root is the LCA.
                return root
