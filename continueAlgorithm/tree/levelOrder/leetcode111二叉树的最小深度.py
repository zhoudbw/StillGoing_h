# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        minDepthValue = 0
        if root:
            queue = [ root ]
            
            def isLeafNode( iNode ):
                return iNode and ( not iNode.left ) and ( not iNode.right )
            
            while queue:
                curQueueSize = len( queue )
                minDepthValue += 1
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if isLeafNode( tNode ): return minDepthValue
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
        return minDepthValue
    