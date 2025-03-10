# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        everyLevelMaxValueList = []
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                # levelMaxValue = -2e31 - 1
                levelMaxValue = float( "-inf" )
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    # if tNode.val > levelMaxValue: levelMaxValue = tNode.val
                    levelMaxValue = max( levelMaxValue, tNode.val )
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
                everyLevelMaxValueList.append( levelMaxValue )
        return everyLevelMaxValueList
                    