# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    
    # -- 前序遍历 ( 通过父节点,判断子节点的性质 ) --
    def sumOfLeftLeaves( self, root ):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        leftChildSum = [ 0 ]
        
        def dfsLeftChildSum( iRoot ):
            if not iRoot: return
            
            tLeftNode = iRoot.left
            if tLeftNode and not tLeftNode.left and not tLeftNode.right:
                leftChildSum[ 0 ] += tLeftNode.val
            dfsLeftChildSum( iRoot.left )
            dfsLeftChildSum( iRoot.right )
        
        dfsLeftChildSum( root )
        return leftChildSum[ 0 ]
    
    # -- 后序遍历 --
    def sumOfLeftLeaves( self, root ):
        if not root: return 0
        leftTreeWithLeftLeafSum  = self.sumOfLeftLeaves( root.left )
        if root.left and not root.left.left and not root.left.right:
            leftTreeWithLeftLeafSum = root.left.val
        rightTreeWithLeftLeafSum = self.sumOfLeftLeaves( root.right )
        return leftTreeWithLeftLeafSum + rightTreeWithLeftLeafSum
    