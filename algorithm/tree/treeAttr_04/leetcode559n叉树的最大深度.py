"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from algorithm.tree.MultiwayTreeNode import MultiwayTreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
            tChildMaxDepth = 0
            if root.children:
                for tChild in root.children:
                    tChildDepth = self.maxDepth( tChild )
                    tChildMaxDepth = max( tChildMaxDepth, tChildDepth )
            return tChildMaxDepth + 1
        return 0
    
    
    def maxDepth2(self, root):
        """
        :type root: Node
        :rtype: int
        """
        maxDepthVal = [ 0 ]
        
        def dfs( iRoot, iDepth ):
            if iRoot:
                maxDepthVal[ 0 ] = max( maxDepthVal[ 0 ], iDepth )
                if iRoot.children:
                    for tChild in iRoot.children:
                        dfs( tChild, iDepth + 1 )
        dfs( root, 1 )
        return maxDepthVal[ 0 ]
    
    def maxDepth3(self, root):
        maxDepthValue = 0
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if tNode.children:
                        for fNode in tNode.children: queue.append( fNode )
                maxDepthValue += 1
        return maxDepthValue


if __name__ == '__main__':
    mRoot = MultiwayTreeNode( val = 1, children = [
        MultiwayTreeNode( 3, [
            MultiwayTreeNode( 5 ),
            MultiwayTreeNode( 6 ),
        ] ),
        MultiwayTreeNode( 2 ),
        MultiwayTreeNode( 4 ),
    ] )
    print( Solution().maxDepth( mRoot ) )
            
    