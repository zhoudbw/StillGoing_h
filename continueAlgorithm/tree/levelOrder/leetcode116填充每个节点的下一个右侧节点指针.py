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
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if i + 1 < curQueueSize: tNode.next = queue[ 0 ]
                    if tNode.left: queue.append( tNode.left )
                    if tNode.right: queue.append( tNode.right )
        return root
    