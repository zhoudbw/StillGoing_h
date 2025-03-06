
def dfsWithIteration( root ):
    nodeValueList = []
    if root:
        stack = [ root ]
        while stack:
            node = stack.pop()
            nodeValueList.append( node.val )
            if node.left: stack.append( node.left )
            if node.right: stack.append( node.right )
    return nodeValueList[ ::-1 ]

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # def dfs( iRoot, iResList ):
        #     if iRoot is None:
        #         return
        #     dfs( iRoot.left, iResList )
        #     dfs( iRoot.right, iResList )
        #     iResList.append( iRoot.val )
        # 
        # resList = []
        # dfs( root, resList )
        # return resList
        
        return dfsWithIteration( root )
    