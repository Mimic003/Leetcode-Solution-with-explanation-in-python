class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # check left, right 
        # if left > node or right < node:
            # return 
        #recurse left and right 
        # return true

        def checkValid(node, minNode, maxNode):
            if not node:
                return True
            
            if minNode >= node.val or maxNode <= node.val:
                return False
            
            return checkValid(node.left, minNode, node.val) and checkValid(node.right, node.val, maxNode)
        
        return checkValid(root, float("-inf"), float("inf"))