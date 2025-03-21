# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from algorithm.tree.TreeNode import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isSymmetricLine( iValueList ):
            iValueListLen = len( iValueList )
            left, right = 0, iValueListLen - 1
            while left <= right:
                if iValueList[ left ] != iValueList[ right ]: return False
                left += 1
                right -= 1
            return True
        
        if root:
            queue = [ root ]
            while queue:
                curQueueSize = len( queue )
                curLevelValueList = []
                for i in range( 0, curQueueSize ):
                    tNode = queue.pop( 0 )
                    if tNode:
                        curLevelValueList.append( tNode.val )
                        queue.append( tNode.left )
                        queue.append( tNode.right )
                    else:
                        curLevelValueList.append( '#' )
                if not isSymmetricLine( curLevelValueList ): return False
        return True
    
    # -- 二叉树是否镜像,联系翻转二叉树的话 => 二叉树翻转后是否和原来的树一样,一样就是对称的 --
    # -- 判断对称二叉树要比较的不是左右节点, 要比较的是根节点的左子树与右子树是不是相互翻转的 --
    # -- 要比较的是两个树（这两个树是根节点的左右子树），所以在递归遍历的过程中，也是要同时遍历两棵树 --
    # -- 比较的是两个子树的里侧和外侧的元素是否相等 --
    # -- 遍历只能是“后序遍历”，因为我们要通过递归函数的返回值来判断两个子树的内侧节点和外侧节点是否相等 --
    # -- 正是因为要遍历两棵树而且要比较内侧和外侧节点，所以准确的来说是一个树的遍历顺序是左右中，一个树的遍历顺序是右左中--
    def isSymmetric2(self, root):
        if root:
            def compare( iLeftRoot, iRightRoot ):
                if not iLeftRoot and iRightRoot: return False
                if iLeftRoot and not iRightRoot: return False
                if not iLeftRoot and not iRightRoot: return True
                if iLeftRoot.val != iRightRoot.val: return False
                # -- 能够走到这里,说明iLeftRoot和iRightRoot相等,可以继续接下来的比较 --
                outsideFlag = compare( iLeftRoot.left, iRightRoot.right )
                insideFlag = compare( iLeftRoot.right, iRightRoot.left )
                return outsideFlag and insideFlag
            return compare( root.left, root.right )
        return True

    # -- 借助队列使用迭代的方式判断是否翻转 --
    def isSymmetric3(self, root):
        if root:
            queue = [ root.left, root.right ]
            while queue:
                # -- 每次取出两个作比较 ( 内侧和外侧比较 ) --
                tLeftNode = queue.pop( 0 )
                tRightNode = queue.pop( 0 )
                if not tLeftNode and not tRightNode: continue
                if ( tLeftNode and not tRightNode ) or ( not tLeftNode and tRightNode ) or ( tLeftNode.val != tRightNode.val ): return False
                # -- 注意塞入队列的顺序 --
                queue.append( tLeftNode.left )
                queue.append( tRightNode.right )
                queue.append( tLeftNode.right )
                queue.append( tRightNode.left )
        return True
    

if __name__ == '__main__':
    mRoot = TreeNode(
        val = 1,
        left = TreeNode(
            val = 2,
            left = TreeNode( 3 ),
            right = TreeNode( 4 ),
        ),
        right = TreeNode(
            val = 2,
            left = TreeNode( 4 ),
            right = TreeNode( 3 ),
        ),
    )
    print( Solution().isSymmetric2( mRoot ) )
                    
                
                
                
                
        
    