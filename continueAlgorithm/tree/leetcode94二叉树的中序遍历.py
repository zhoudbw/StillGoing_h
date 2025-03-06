
def dfsWithIteration( root ):
    nodeValueList = []
    if root:
        stack = []
        curNode = root
        while curNode or stack:
            if curNode:
                stack.append( curNode )
                curNode = curNode.left
            else:
                node = stack.pop()
                nodeValueList.append( node.val )
                curNode = node.right
    return nodeValueList


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return dfsWithIteration( root )