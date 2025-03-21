# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # -- 注意: 前序求深度, 后序求高度 --
        def dfsHeight( iRoot ):
            if iRoot:
                iLeftHeight = dfsHeight( iRoot.left )
                if iLeftHeight == -1: return -1
                iRightHeight = dfsHeight( iRoot.right )
                if iRightHeight == -1: return -1
                
                if abs( iLeftHeight - iRightHeight ) > 1: return -1
                else:
                    return max( iLeftHeight, iRightHeight ) + 1
            return 0
            
        return dfsHeight( root ) != -1
        