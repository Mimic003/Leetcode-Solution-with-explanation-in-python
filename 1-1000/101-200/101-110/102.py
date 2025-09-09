class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            levelNodes = len(q)
            level = []
            for i in range(levelNodes):
                curr = q.popleft()
                
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                res.append(level)
        return res