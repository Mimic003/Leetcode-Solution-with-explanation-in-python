class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_i = {}
        for i, val in enumerate(inorder):
            val_to_i[val] = i

        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end or inorder_start > inorder_end: return None

            head = TreeNode(preorder[preorder_start])
            i = val_to_i[preorder[preorder_start]]
            left_size = i - inorder_start

            head.left = helper(preorder_start + 1, preorder_start + left_size, inorder_start, i - 1)
            head.right = helper(preorder_start + left_size + 1, preorder_end, i + 1, inorder_end)


            return head
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)