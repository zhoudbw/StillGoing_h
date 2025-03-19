# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        everyLevelValueList = []
        if root:
            def dfs( iNode, iDepth ):
                if iNode is None: return
                if iDepth == len( everyLevelValueList ): everyLevelValueList.append( [] )
                
                everyLevelValueList[ iDepth ].append( iNode.val )
                dfs( iNode.left, iDepth + 1 )
                dfs( iNode.right, iDepth + 1 )
            dfs( root, 0 )
        return everyLevelValueList[ ::-1 ]