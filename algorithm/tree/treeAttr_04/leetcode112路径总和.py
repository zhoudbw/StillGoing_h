# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    
    # -- 不带返回值 --
    def hasPathSum( self, root, targetSum ):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        hasMatchPathFlag = [ False ]
        
        def dfsTargetSum( iRoot, iTarget, iCurSum ):
            if not iRoot: return
            
            iCurSum += iRoot.val
            if not iRoot.left and not iRoot.right:
                hasMatchPathFlag[ 0 ] = hasMatchPathFlag[ 0 ] or iTarget == iCurSum
            dfsTargetSum( iRoot.left, iTarget, iCurSum )
            dfsTargetSum( iRoot.right, iTarget, iCurSum )
        
        dfsTargetSum( root, targetSum, 0 )
        return hasMatchPathFlag[ 0 ]
    
    # -- 带返回值: 找到一个符合的路径就返回 --
    def hasPathSum( self, root, targetSum ):
        if not root: return False
        
        def dfsHasPathSum( iRoot, iCurLeftVal ):
            iCurLeftVal -= iRoot.val
            if not iRoot.left and not iRoot.right and iCurLeftVal == 0: return True
            if not iRoot.left and not iRoot.right: return False
            
            if iRoot.left and dfsHasPathSum( iRoot.left, iCurLeftVal ): return True
            if iRoot.right and dfsHasPathSum( iRoot.right, iCurLeftVal ): return True
            
            return False
        
        return dfsHasPathSum( root, targetSum )
    
    # -- 简化写法 --
    def hasPathSum( self, root, targetSum ):
        if not root: return False
        
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0: return True
        if not root.left and not root.right: return False
        
        if root.left and self.hasPathSum( root.left, targetSum ): return True
        if root.right and self.hasPathSum( root.right, targetSum ): return True
        
        return False
    
    # -- 再简化 --
    def hasPathSum( self, root, targetSum ):
        if not root: return False
        
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0: return True
        return self.hasPathSum( root.left, targetSum ) or self.hasPathSum( root.right, targetSum )
                