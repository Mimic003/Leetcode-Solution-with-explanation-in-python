class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        from collections import deque
        q = deque([root])
        idx = 0
        while q:
            size = len(q)
            layer = []
            for i in range(size):
                node = q.popleft()
                layer.append(node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            if idx % 2 != 0:
                res.append(list(reversed(layer)))
            else:
                res.append(layer)
            idx += 1
        return res