"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # -- 本题说“二叉树”，116题说“完美二叉树”，没有任何差别，一样的逻辑 --
        if root:
            queue = [ root ]
            while queue:
                tPreNode = None
                curQueueSize = len( queue )
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if tPreNode: tPreNode.next = tNode
                    tPreNode = tNode
                    # --
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
        return root
                    