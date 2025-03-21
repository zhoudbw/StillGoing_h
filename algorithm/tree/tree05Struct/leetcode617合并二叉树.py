# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from algorithm.tree.TreeNode import TreeNode


class Solution( object ):
    def mergeTrees( self, root1, root2 ):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        if not root1 and not root2: return None
        if root1 and not root2: return root1
        if root2 and not root1: return root2
        
        newRoot = TreeNode( root1.val + root2.val )
        newRoot.left = self.mergeTrees( root1.left, root2.left )
        newRoot.right = self.mergeTrees( root1.right, root2.right )
        return newRoot
    
    # -- 复用root1 --
    def mergeTrees( self, root1, root2 ):
        if not root1: return root2
        if not root2: return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees( root1.left, root2.left )
        root1.right = self.mergeTrees( root1.right, root2.right )
        return root1
    
    # -- 中序 --
    def mergeTrees( self, root1, root2 ):
        if not root1: return root2
        if not root2: return root1
        
        root1.left = self.mergeTrees( root1.left, root2.left )
        root1.val += root2.val
        root1.right = self.mergeTrees( root1.right, root2.right )
        return root1
    
    # -- 后序 --
    def mergeTrees( self, root1, root2 ):
        if not root1: return root2
        if not root2: return root1
        
        root1.left = self.mergeTrees( root1.left, root2.left )
        root1.right = self.mergeTrees( root1.right, root2.right )
        root1.val += root2.val
        return root1
    
    # -- 层序 --
    def mergeTrees( self, root1, root2 ):
        if not root1: return root2
        if not root2: return root1
        
        queue = [ root1, root2 ]
        while queue:
            tNode1, tNode2 = queue.pop( 0 ), queue.pop( 0 )
            tNode1.val += tNode2.val
            
            if tNode1.left and tNode2.left:
                queue.append( tNode1.left )
                queue.append( tNode2.left )
            if tNode1.right and tNode2.right:
                queue.append( tNode1.right )
                queue.append( tNode2.right )
            
            if not tNode1.left and tNode2.left:
                tNode1.left = tNode2.left
            if not tNode1.right and tNode2.right:
                tNode1.right = tNode2.right
        return root1
    