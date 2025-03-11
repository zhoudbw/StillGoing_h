# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # -- 后序 --
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None: return None
        leftNode = self.invertTree( root.left )
        rightNode = self.invertTree( root.right )
        root.left = rightNode
        root.right = leftNode
        return root

    # -- 层序 --
    def invertTree2(self, root):
        if root:
            queue = [ root ]
            while queue:
                tNode = queue.pop( 0 )
                tNode.left, tNode.right = tNode.right, tNode.left
                if tNode.left: queue.append( tNode.left )
                if tNode.right: queue.append( tNode. right )
        return root

    # -- 前序 --
    def invertTree3(self, root):
        if root is None: return None
        root.left, root.right = root.right, root.left
        self.invertTree3( root.left )
        self.invertTree3( root.right )
        return root
    
    # -- 前序迭代法 --
    def invertTree4(self, root):
        if root:
            stack = [ root ]
            while stack:
                tNode = stack.pop()
                tNode.left, tNode.right = tNode.right, tNode.left
                if tNode.right: stack.append( tNode.right )
                if tNode.left: stack.append( tNode.left )
        return root
        
    # -- 如果使用中序递归某些节点会被重复翻转,下述代码更改可以避免这个问题 --
    def invertTree4(self, root ):
        if root is None: return None
        self.invertTree4( root.left )
        root.left, root.right = root.right, root.left
        # -- 注意 这里依然要遍历左孩子，因为中间节点已经翻转了 --
        self.invertTree4( root.left )
        return root
    
    # -- 使用中序迭代遍历需要特别注意代码处理顺序 --
    def invertTree5(self, root ):
        if root:
            stack = []
            tCurNode = root
            while stack or tCurNode:
                if tCurNode:
                    stack.append( tCurNode )
                    tCurNode = tCurNode.left
                else:
                    tNode = stack.pop()
                    # -- 这里需要特别注意一下,顺序 line:71,line:72 不能交换 --
                    tCurNode = tNode.right
                    tNode.left, tNode.right = tNode.right, tNode.left
        return root
            
            
    