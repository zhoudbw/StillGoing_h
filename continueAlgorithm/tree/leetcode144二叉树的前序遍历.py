def dfsWithIteration( root ):
    nodeValueList = []
    if root:
        stack = [ root ]
        while stack:
            node = stack.pop()
            nodeValueList.append( node.val )
            if node.right: stack.append( node.right )
            if node.left: stack.append( node.left )
    return nodeValueList


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return dfsWithIteration( root )

        