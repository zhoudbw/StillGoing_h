# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    def getMinimumDifference( self, root ):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        inorderList = []
        
        def inorder( iRoot ):
            if not iRoot: return
            
            inorder( iRoot.left )
            inorderList.append( iRoot.val )
            inorder( iRoot.right )
        
        inorder( root )
        
        minDiff = float( 'inf' )
        for i in range( 1, len( inorderList ) ):
            diff = abs( inorderList[ i ] - inorderList[ i - 1 ] )
            if diff < minDiff:
                minDiff = diff
        return minDiff
    
    
    # -- 以上代码是把二叉搜索树转化为有序数组了，其实在二叉搜素树中序遍历的过程中，可以直接计算，需要用一个pre节点记录一下cur节点的前一个节点。 --
    def getMinimumDifference( self, root ):
        
        tVariableDict = {
                "dMinDiff": float( 'inf' ),
                "dPreNode": None
        }
        
        def dfsInorder( iCurNode ):
            if not iCurNode: return
            dfsInorder( iCurNode.left )
            if tVariableDict[ "dPreNode" ]:
                tVariableDict[ "dMinDiff" ] = min( tVariableDict[ "dMinDiff" ], abs( tVariableDict[ "dPreNode" ].val - iCurNode.val ) )
            tVariableDict[ "dPreNode" ] = iCurNode
            dfsInorder( iCurNode.right )
        
        dfsInorder( root )
        return tVariableDict[ "dMinDiff" ]
    
    # -- 中序遍历的迭代法 --
    def getMinimumDifference( self, root ):
        stack = []
        tCurNode, tPreNode = root, None
        minDiff = float( 'inf' )
        while stack or tCurNode:
            if tCurNode:
                stack.append( tCurNode )
                tCurNode = tCurNode.left
            else:
                tCurNode = stack.pop()
                if tPreNode:
                    minDiff = min( minDiff, abs( tPreNode.val - tCurNode.val ) )
                tPreNode = tCurNode
                tCurNode = tCurNode.right
        return minDiff
        
            
            
        
        