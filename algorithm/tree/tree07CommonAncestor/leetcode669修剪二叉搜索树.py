# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    def trimBST( self, root, low, high ):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        
        if not root: return None
        if root.val < low:
            # -- 递归右子树,返回符合条件的节点 --
            return self.trimBST( root.right, low, high )
        if root.val > high:
            # -- 递归左子树,返回符合条件的节点 --
            return self.trimBST( root.left, low, high )
        
        root.left = self.trimBST( root.left, low, high )
        root.right = self.trimBST( root.right, low, high )

        return root
    