# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from algorithm.tree.TreeNode import TreeNode


class Solution( object ):
    # -- 插入节点,目标就是找到待插入节点的父节点,这样才能链接子节点 --
    def insertIntoBST( self, root, val ):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        nodeToBeInserted = TreeNode( val )
        if not root: return nodeToBeInserted
        
        tCurNode = root
        while tCurNode:
            if tCurNode.val > val:
                if not tCurNode.left:
                    tCurNode.left = nodeToBeInserted
                    return root
                tCurNode = tCurNode.left
            if tCurNode.val < val:
                if not tCurNode.right:
                    tCurNode.right = nodeToBeInserted
                    return root
                tCurNode = tCurNode.right
        return root
    
    def insertIntoBST( self, root, val ):
        if not root:
            node = TreeNode( val )
            return node
        
        # -- 找到符合的位置,将node链接上去 --
        if root.val > val:
            root.left = self.insertIntoBST( root.left, val )
        if root.val < val:
            root.right = self.insertIntoBST( root.right, val )
        return root
    
        