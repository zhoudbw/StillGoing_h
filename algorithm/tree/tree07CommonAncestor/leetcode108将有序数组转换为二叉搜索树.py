# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# -- 一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。 --
from algorithm.tree.TreeNode import TreeNode


class Solution( object ):
    def sortedArrayToBST( self, nums ):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums: return None
        if len( nums ) == 1: return TreeNode( nums[ 0 ] )
        
        midIndex = len( nums ) // 2
        root = TreeNode( nums[ midIndex ] )
        
        root.left = self.sortedArrayToBST( nums[ : midIndex ] )
        root.right = self.sortedArrayToBST( nums[ midIndex + 1: ] )
        return root
    
    def sortedArrayToBST( self, nums ):
        if not nums: return None
        
        # -- 区间严格遵守左闭右开 --
        def buildTree( iNums, iStart, iEnd ):
            if iStart >= iEnd: return None
            
            midIndex = iStart + ( iEnd - iStart ) // 2
            root = TreeNode( iNums[ midIndex ] )
            
            root.left = buildTree( iNums, iStart, midIndex )
            root.right = buildTree( iNums, midIndex + 1, iEnd )
            return root
        
        return buildTree( nums, 0, len( nums ) )
    