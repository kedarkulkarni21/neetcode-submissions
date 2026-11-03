# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(root):
            nonlocal max_len

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            curr_diam = left + right
            max_len = max(max_len, curr_diam)

            return 1 + max(left, right)

        dfs(root)
        return max_len