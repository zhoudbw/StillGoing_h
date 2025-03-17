# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        
        def dfsPath( iRoot, iPath, iPathSet ):
            # -- 题目节点数量范围: [ 1, 100 ] --
            iPath.append( iRoot.val )
            if not iRoot.left and not iRoot.right:
                iPathSet.append( "->".join( map( str, iPath ) ) )
                return
            if iRoot.left:
                dfsPath( iRoot.left, iPath, iPathSet )
                iPath.pop()
            if iRoot.right:
                dfsPath( iRoot.right, iPath, iPathSet )
                iPath.pop()
        
        pathSet = []
        dfsPath( root, [], pathSet )
        return pathSet

    def binaryTreePaths(self, root):
        # -- 题目节点数量范围: [ 1, 100 ] --
        nodeStack  = [ root ]
        pathStack  = [ str( root.val ) ]
        allPathSet = []
        while nodeStack:
            tNode = nodeStack.pop()
            tPath = pathStack.pop()
            if not tNode.left and not tNode.right:
                allPathSet.append( tPath )
            if tNode.right:
                nodeStack.append( tNode.right )
                pathStack.append( tPath + "->" + str( tNode.right.val ) )
            if tNode.left:
                nodeStack.append( tNode.left )
                pathStack.append( tPath + "->" + str( tNode.left.val ) )
        return allPathSet
            
    