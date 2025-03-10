
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfsWithIteration( iRoot ):
            nodeValueList = []
            if iRoot:
                stack = [ iRoot ]
                while stack:
                    tNode = stack.pop()
                    nodeValueList.append( tNode.val )
                    if tNode.right: stack.append( tNode.right )
                    if tNode.left: stack.append( tNode.left )
            return nodeValueList
        return dfsWithIteration( root )

        