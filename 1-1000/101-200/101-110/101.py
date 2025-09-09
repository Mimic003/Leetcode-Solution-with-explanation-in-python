class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def DFS(root1,root2):
            if root1 is None and root2 is None:
                return True
            if (not root1 and root2) or (root1 and not root2) or root1.val != root2.val:
                return False
            return DFS(root1.left,root2.right) and DFS(root1.right,root2.left)
        if root is None:
            return True
        return DFS(root.left,root.right)