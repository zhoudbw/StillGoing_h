

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfs( iRoot, iResList ):
            if iRoot is None:
                return
            dfs( iRoot.left, iResList )
            dfs( iRoot.right, iResList )
            iResList.append( iRoot.val )

        resList = []
        dfs( root, resList )
        return resList
    