# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from algorithm.tree.TreeNode import TreeNode


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        sameValNodeList = []
        
        def findSubRoot( iRoot, iSubRoot ):
            if iRoot:
                iQueue = [ iRoot ]
                while iQueue:
                    iTNode = iQueue.pop( 0 )
                    if iTNode.val == iSubRoot.val: sameValNodeList.append( iTNode )
                    if iTNode.left: iQueue.append( iTNode.left )
                    if iTNode.right: iQueue.append( iTNode.right )
        findSubRoot( root, subRoot )
        
        def compare( iChildRoot, iSubRoot ):
            if not iChildRoot and not iSubRoot: return True
            if ( not iChildRoot and iSubRoot ) or ( iChildRoot and not iSubRoot ) or ( iChildRoot.val != iSubRoot.val ): return False
            leftSameFlag = compare( iChildRoot.left, iSubRoot.left )
            rightSameFlag = compare( iChildRoot.right, iSubRoot.right )
            return leftSameFlag and rightSameFlag
        
        isSameFlag = False
        for tNode in sameValNodeList:
            isSameFlag = isSameFlag or compare( tNode, subRoot )
        return isSameFlag
    
    
if __name__ == '__main__':
    mRoot = TreeNode( val=1, left=TreeNode( 1 ) )
    mSubRoot = TreeNode( 1 )
    print( Solution().isSubtree( mRoot, mSubRoot ) )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    