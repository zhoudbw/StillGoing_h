# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root:
            leftTreeNodeCount = self.countNodes( root.left )
            rightTreeNodeCount = self.countNodes( root.right )
            return leftTreeNodeCount + rightTreeNodeCount + 1
        return 0

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        totalCount = [ 0 ]
        if root:
            def dfs( iRoot ):
                if iRoot:
                    totalCount[ 0 ] = totalCount[ 0 ] + 1
                    dfs( iRoot.left )
                    dfs( iRoot.right )
            dfs( root )
        return totalCount[ 0 ]

    # -- 利用完全二叉树的性质求解个数,对于慢二叉树,节点数量为 ( 2^depth - 1 ) --
    def countNodes(self, root):
        if root:
            tLeftRoot, tRightRoot = root.left, root.right
            leftDepth, rightDepth = 0, 0
            while tLeftRoot:
                leftDepth += 1
                tLeftRoot = tLeftRoot.left
            while tRightRoot:
                rightDepth += 1
                tRightRoot = tRightRoot.right
            if leftDepth == rightDepth:
                return ( 2 << leftDepth ) - 1
            leftNodeCount = self.countNodes( root.left )
            rightNodeCount = self.countNodes( root.right )
            return leftNodeCount + rightNodeCount + 1
            
        return 0
    