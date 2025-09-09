class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        inorder_index = {val: i for i, val in enumerate(inorder)}

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            idx = inorder_index[root_val]

            root.right = build(idx + 1, in_right)
            root.left = build(in_left, idx - 1)

            return root

        return build(0, len(inorder) - 1)