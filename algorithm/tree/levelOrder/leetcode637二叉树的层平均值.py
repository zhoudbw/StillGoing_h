# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        everyLevelAvgList = []
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                thisLevelSum = 0
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    thisLevelSum += tNode.val
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
                everyLevelAvgList.append( thisLevelSum / float( curQueueSize ) )
        return everyLevelAvgList
    