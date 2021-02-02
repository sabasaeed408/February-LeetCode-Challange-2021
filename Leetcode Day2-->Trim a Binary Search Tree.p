class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        #check it the tree is empty or not 
            if root is None:
                return None
         #If the curent node value is loo small then left is terminted we proceed with right
            if root.val < L:
                return trim(root.right, L, R)
         #same happen here we proceed with left
            elif root.val > R:
                return trim(root.left, L, R)
            #if the cureent node is within bound we have to check on both subtree
            else:
                root.left = trim(root.left, L, R)
                root.right = trim(root.right, L, R)
                return root
      
