# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    
    # -- 利用二叉搜索树的形式: 中序遍历是有序的序列 --
    def isValidBST( self, root ):
        inorderList = [ ]
        
        def dfsInorder( iRoot ):
            if iRoot: return
            dfsInorder( iRoot.left )
            inorderList.append( iRoot.val )
            dfsInorder( iRoot.right )
        
        dfsInorder( root )
        
        validFlag = True
        for i in range( 1, len( inorderList ) ):
            if inorderList[ i - 1 ] >= inorderList[ i ]:
                validFlag = False
        return validFlag
    
    # -- 上述代码可以在中序遍历的过程中进行判断 --
    def isValidBST( self, root ):
        pass
        
        
        