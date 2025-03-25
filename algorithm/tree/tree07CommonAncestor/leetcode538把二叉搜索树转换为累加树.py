# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    def convertBST( self, root ):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # -- 二叉搜索树按照中序遍历 左根右遍历是递增的 --
        # -- 那么二叉搜索树按照 右根左遍历,就是递减的 --
        # -- 从最大数值的节点开始累加 --
        self.accumulateValue = 0

        def dfsAccumulate( iRoot ):
            if not iRoot: return
            dfsAccumulate( iRoot.right )

            self.accumulateValue += iRoot.val
            iRoot.val = self.accumulateValue

            dfsAccumulate( iRoot.left )

        dfsAccumulate( root )
        return root

    # -- 迭代法, 就是中序遍历的模仿 --
    def convertBST( self, root ):
        accumulateValue = 0
        stack = []
        curNode = root
        while stack or curNode:
            if curNode:
                stack.append( curNode )
                curNode = curNode.right
            else:
                curNode = stack.pop()
                accumulateValue += curNode.val
                curNode.val = accumulateValue
                curNode = curNode.left
        return root
