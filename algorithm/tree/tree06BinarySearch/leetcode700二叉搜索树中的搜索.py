# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    def searchBST( self, root, val ):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root: return None
        if root.val == val: return root
        if root.val > val: return self.searchBST( root.left, val )
        if root.val < val: return self.searchBST( root.right, val )
    
    
    def searchBST( self, root, val ):
        if not root: return None
        while root:
            if root.val == val: return root
            elif root.val > val: root = root.left
            elif root.val < val: root = root.right
        return None
        
        
        