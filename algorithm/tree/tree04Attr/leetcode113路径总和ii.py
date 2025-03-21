# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    def pathSum( self, root, targetSum ):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        def dfsPathSum( iRoot, iTargetSum, iPath, iPathSet ):
            if not iRoot: return
            
            iPath.append( iRoot.val )
            if not iRoot.left and not iRoot.right:
                if sum( iPath ) == iTargetSum:
                    iPathSet.append( iPath[ :: ] )
            
            if iRoot.left:
                dfsPathSum( iRoot.left, iTargetSum, iPath, iPathSet )
                iPath.pop()     # -- 前序遍历时,向上回溯走这里 --
            if iRoot.right:
                dfsPathSum( iRoot.right, iTargetSum, iPath, iPathSet )
                iPath.pop()
        
        pathSet = []
        dfsPathSum( root, targetSum, [], pathSet )
        return pathSet
    