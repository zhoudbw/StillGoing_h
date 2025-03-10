# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxDepthValue = [ 0 ]
        if root:
            def dfs( iNode, iDepth ):
                if iNode is None: return
                if iDepth == maxDepthValue[ 0 ]: maxDepthValue[ 0 ] += 1
                dfs( iNode.left, iDepth + 1 )
                dfs( iNode.right, iDepth + 1 )
            dfs( root, 0 )
        return maxDepthValue[ 0 ]

    def maxDepth2(self, root):
        maxDepthValue = [ 0 ]
        if root:
            def dfs( iNode, iDepth ):
                if iNode is None: return
                maxDepthValue[ 0 ] = max( maxDepthValue[ 0 ], iDepth )
                dfs( iNode.left, iDepth + 1 )
                dfs( iNode.right, iDepth + 1 )
            dfs( root, 1 )
        return maxDepthValue[ 0 ]

    def maxDepth3(self, root):
        def dfs( iNode, iDepth ):
            if iNode is None: return iDepth
            leftMaxDepthValue = dfs( iNode.left, iDepth + 1 )
            rightMaxDepthValue = dfs( iNode.right, iDepth + 1 )
            return max( leftMaxDepthValue, rightMaxDepthValue )
        return dfs( root, 0 )

    def maxDepth4(self, root):
        maxDepthValue = 0
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
                maxDepthValue += 1
        return maxDepthValue
            
                    
                
                