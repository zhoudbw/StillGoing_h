# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution( object ):
    def lowestCommonAncestor( self, root, p, q ):
        
        # -- 按照普通二叉树的做法去处理,直接后序遍历,自底向上回溯 --
        if not root or root == p or root == q: return root
        
        left = self.lowestCommonAncestor( root.left, p, q )
        right = self.lowestCommonAncestor( root.right, p, q )
        if left and right: return root
        if left and not right: return left
        else: return right
    
    def lowestCommonAncestor( self, root, p, q ):
        """
        因为是有序树，所以 如果 中间节点是 q 和 p 的公共祖先，那么 中节点的数组 一定是在 [p, q]区间的。
        即 中节点 > p && 中节点 < q 或者 中节点 > q && 中节点 < p。
        那么只要从上到下去遍历，遇到 cur节点是数值在[p, q]区间中则一定可以说明该节点cur就是p 和 q的公共祖先。 
        那问题来了，一定是最近公共祖先吗？   —— 是的
        
        既然这样的话,使用什么遍历都已经无所谓了,只要找到节点满足 min(p, q) <= x <= max(p, q)即可
        """
        while root:
            if root.val > max( p.val, q.val ): root = root.left
            elif root.val < min( p.val, q.val ): root = root.right
            else: return root
        return None
        
        