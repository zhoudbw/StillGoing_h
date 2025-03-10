"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        everyLevelValueList = []
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                levelValueList = []
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    levelValueList.append( tNode.val )
                    if tNode.children:
                        for child in tNode.children:
                            if child: queue.append( child )
                everyLevelValueList.append( levelValueList )
        return everyLevelValueList
    
    def levelOrder2(self, root ):
        everyLevelValueList = []
        if root:
            def dfs( iNode, iDepth ):
                if iNode is None: return
                if iDepth == len( everyLevelValueList ): everyLevelValueList.append( [] )
                
                everyLevelValueList[ iDepth ].append( iNode.val )
                if iNode.children:
                    for child in iNode.children:
                        dfs( child, iDepth + 1 )
            dfs( root, 0 )
        return everyLevelValueList
    