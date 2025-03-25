# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    
    # -- 递归法 --
    def deleteNode( self, root, key ):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # -- 1. 没有找到目标节点 --
        if not root: return None
        
        if root.val == key:
            # -- 2. 左右孩子不存在 ( 叶子结点 ) --
            if not root.left and not root.right: return None
            # -- 3. 左孩子存在,右孩子不存在 --
            if root.left and not root.right: return root.left
            # -- 4. 右孩子存在,左孩子不存在 --
            if root.right and not root.left: return root.right
            # -- 5. 左孩子存在,右孩子存在 --
            if root.left and root.right:
                # --
                tRightChildMaxLeftNode = root.right
                while tRightChildMaxLeftNode.left:
                    tRightChildMaxLeftNode = tRightChildMaxLeftNode.left
                tRightChildMaxLeftNode.left = root.left
                return root.right
                
        elif root.val > key: root.left = self.deleteNode( root.left, key )
        elif root.val < key: root.right = self.deleteNode( root.right, key )
        return root
    
    # -- 迭代法 --
    def deleteNode( self, root, key ):
        def deleteOneNode( iTargetNode ):
            if not iTargetNode: return None
            if not iTargetNode.left and not iTargetNode.right: return None
            if iTargetNode.left and not iTargetNode.right: return iTargetNode.left
            if iTargetNode.right and not iTargetNode.left: return iTargetNode.right
            if iTargetNode.left and iTargetNode.right:
                tNode = iTargetNode.right
                while tNode.left:
                    tNode = tNode.left
                tNode.left = iTargetNode.left
                return iTargetNode.right
        
        if not root: return None
        curNode, parentNode = root, None
        
        # -- 找到目标节点和父节点 --
        while curNode:
            if curNode.val == key: break
            parentNode = curNode
            if curNode.val > key: curNode = curNode.left
            else: curNode = curNode.right
        
        if not parentNode:
            # -- 删除的节点是根节点 --
            return deleteOneNode( root )
        else:
            if parentNode.left and parentNode.left.val == key:
                parentNode.left = deleteOneNode( curNode )
            elif parentNode.right and parentNode.right.val == key:
                parentNode.right = deleteOneNode( curNode )
        return root
        
    
        