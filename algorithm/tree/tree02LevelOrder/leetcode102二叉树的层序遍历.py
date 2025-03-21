# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # -- 迭代法 --
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        everyLevelValueList = []
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                levelValueList = []
                for i in range( 0, curQueueSize ):
                    node = queue.pop( 0 )
                    levelValueList.append( node.val )
                    if node.left is not None: queue.append( node.left )
                    if node.right is not None: queue.append( node.right )
                everyLevelValueList.append( levelValueList )
        return everyLevelValueList
    
    # -- 递归法 --
    def levelOrderRec(self, root ):
        everyLevelValueList = []
        if root:
            def dfs( iNode, iDepth ):
                if iNode is None: return
                if iDepth == len( everyLevelValueList ): everyLevelValueList.append( [] )

                everyLevelValueList[ iDepth ].append( iNode.val )
                dfs( iNode.left, iDepth + 1 )
                dfs( iNode.right, iDepth + 1 )
            dfs( root, 0 )
        return everyLevelValueList
                
                
            
            
            