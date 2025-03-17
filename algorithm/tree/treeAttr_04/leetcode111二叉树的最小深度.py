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
        if root:
            leftHeight  = self.minDepth( root.left )
            rightHeight = self.minDepth( root.right )
            
            # -- 特别注意这里和最大深度不一样 --
            # -- 遍历的顺序为后序,求二叉树的最小深度和求二叉树的最大深度的差别主要在于处理左右孩子不为空的逻辑 --
            # --最小深度是从根节点到最近叶子节点的最短路径上的节点数量。注意是叶子节点。
            if root.left and not root.right: return leftHeight + 1
            if not root.left and root.right: return rightHeight + 1
            return min( leftHeight, rightHeight ) + 1
        return 0

    def minDepth2(self, root):
        if not root: return 0
        
        minDepthValue = [ float( 'inf' ) ]
        
        def dfs( iRoot, iDepth ):
            if iRoot:
                if not iRoot.left and not iRoot.right: minDepthValue[ 0 ] = min( minDepthValue[ 0 ], iDepth )
                if iRoot.left: dfs( iRoot.left, iDepth + 1 )
                if iRoot.right: dfs( iRoot.right, iDepth + 1 )
        dfs( root, 1 )
        return minDepthValue[ 0 ]
    
    def minDepth3(self, root):
        if root:
            queue = [ ( root, 1 ) ]
            while queue:
                tNode, tDepth = queue.pop( 0 )
                if not tNode.left and not tNode.right: return tDepth
                if tNode.left: queue.append( ( tNode.left, tDepth + 1 ) )
                if tNode.right: queue.append( ( tNode.right, tDepth + 1 ) )
        return 0
    