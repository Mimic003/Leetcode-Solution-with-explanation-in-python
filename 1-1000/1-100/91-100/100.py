class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False
            return issame(p.left,q.left) and issame(p.right,q.right)
        return issame(p,q)