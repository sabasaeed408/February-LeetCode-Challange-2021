# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.max_ = 0
        def inOrder(node)->int:
            if not node:
                return
            inOrder(node.right)
            node.val+=self.max_
            self.max_= node.val
            inOrder(node.left)
        inOrder(root)
        return root
        
