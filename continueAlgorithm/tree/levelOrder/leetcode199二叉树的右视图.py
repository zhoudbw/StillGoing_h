# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # -- 迭代法 --
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        rightSideValueList = []
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if i == curQueueSize - 1:
                        rightSideValueList.append( tNode.val )
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
        return rightSideValueList
    
    # -- 递归法 --
    def rightSideView2(self, root ):
        rightSideValueList = []
        if root:
            def dfs( iNode, iDepth ):
                if iNode is None: return
                if iDepth == len( rightSideValueList ):
                    rightSideValueList.append( iNode.val )
                dfs( iNode.right, iDepth + 1 )
                dfs( iNode.left, iDepth + 1 )
            dfs( root, 0 )
        return rightSideValueList
    