# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        res = []
        def dfs(root,flag):
            if not root:
                return None
            todelete = (root.val in s)
            root.left = dfs(root.left, todelete)
            root.right = dfs(root.right, todelete)
            if not todelete and flag:
                res.append(root)
            return None if todelete else root
        dfs(root, True)
        return res