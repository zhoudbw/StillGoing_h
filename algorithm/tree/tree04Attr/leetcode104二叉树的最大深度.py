# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # -- 前序后序都可以满足ac --
    # -- 但是根据概念来说,前序求的是深度,后序求的是高度 --
    
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxDepth = [ 0 ]
        
        def dfs( iRoot, iDepth ):
            if iRoot:
                maxDepth[ 0 ] = max( maxDepth[ 0 ], iDepth )
                dfs( iRoot.left, iDepth + 1 )
                dfs( iRoot.right, iDepth + 1 )
            return maxDepth[ 0 ]
        dfs( root, 1 )
        return maxDepth[ 0 ]
    
    
    def maxHeight(self, root ):
        if root:
            leftHeight  = self.maxHeight( root.left )
            rightHeight = self.maxHeight( root.right )
            return max( leftHeight, rightHeight ) + 1
        return 0

        
            
        
        