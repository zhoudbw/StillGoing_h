
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfsWithIteration( iRoot ):
            nodeValueList = []
            if iRoot:
                stack = []
                curNode = iRoot
                while curNode or stack:
                    if curNode:
                        stack.append( curNode )
                        curNode = curNode.left
                    else:
                        node = stack.pop()
                        nodeValueList.append( node.val )
                        curNode = node.right
            return nodeValueList
        return dfsWithIteration( root )