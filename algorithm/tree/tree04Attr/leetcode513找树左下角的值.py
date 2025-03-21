# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    
    # -- 层序遍历 --
    def findBottomLeftValue( self, root ):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        leftValue = [ 0 ]
        transThisLevelFlagList = []
        
        def dfsLeftValue( iRoot, iDepth ):
            if not iRoot: return
            
            if len( transThisLevelFlagList ) == iDepth:
                transThisLevelFlagList.append( True )
                leftValue[ 0 ] = iRoot.val
            dfsLeftValue( iRoot.left, iDepth + 1 )
            dfsLeftValue( iRoot.right, iDepth + 1 )
        
        dfsLeftValue( root, 0 )
        return leftValue[ 0 ]
    
    # -- 利用求二叉树最大深度的方式求解此题 --
    def findBottomLeftValue( self, root ):
        maxDepth    = [ 0 ]
        leftValue   = [ 0 ]
        
        def dfsMaxDepth( iRoot, iDepth ):
            if not iRoot: return 0
            if iDepth > maxDepth[ 0 ]:
                maxDepth[ 0 ] = iDepth
                leftValue[ 0 ] = iRoot.val
            dfsMaxDepth( iRoot.left, iDepth + 1 )
            dfsMaxDepth( iRoot.right, iDepth + 1 )
            
        dfsMaxDepth( root, 1 )
        return leftValue[ 0 ]
    
        
    