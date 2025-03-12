# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def compare( iPRoot, iQRoot ):
            if not iPRoot and not iQRoot: return True
            if ( not iPRoot and iQRoot ) or ( iPRoot and not iQRoot ) or ( iPRoot.val != iQRoot.val ): return False
            
            leftSameFlag = compare( iPRoot.left, iQRoot.left )
            rightSameFlag = compare( iPRoot.right, iQRoot.right )
            return leftSameFlag and rightSameFlag
        return compare( p, q )
    