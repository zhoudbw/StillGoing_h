# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from algorithm.tree.TreeNode import TreeNode


class Solution( object ):
    def buildTree( self, inorder, postorder ):
        """
        inorder 和 postorder 都由 不同 的值组成
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder: return None
        
        rootVal = postorder[ -1 ]
        delimiterIndex = inorder.index( rootVal )
        inorderLeft = inorder[ : delimiterIndex ]
        inorderRight = inorder[ delimiterIndex + 1: ]
        postorderLeft = postorder[ : len( inorderLeft ) ]
        postorderRight = postorder[ len( inorderLeft ): -1 ]
        
        left = self.buildTree( inorderLeft, postorderLeft )
        right = self.buildTree( inorderRight, postorderRight )
        
        return TreeNode( rootVal, left, right )