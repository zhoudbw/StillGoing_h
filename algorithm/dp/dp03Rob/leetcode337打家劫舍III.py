# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    """
        --[[
            小偷又发现了一个新的可行窃的地区;这个地区只有一个入口,我们称之为 root ;
            除了 root 之外,每栋房子有且只有一个“父“房子与之相连;一番侦察之后,
            聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”;
            如果 两个直接相连的房子在同一天晚上被打劫 ,房屋将自动报警;
            给定二叉树的 root ;返回 在不触动警报的情况下 ,小偷能够盗取的最高金额 ;
        ]]
        -- 二叉树相关,首先考虑 前中后序 or 层序 是否可以解决;
        -- 如果偷当前节点,左右孩子就不能偷; 如果不偷取当前节点, 左右孩子就可以考虑偷;
        -- 对于二叉树和动态规划的结合,
            * 定义dp数组, dp[0]表示不偷当前节点能得到的最高金额;
                         dp[1]表示偷取当前节点能得到的最高金额;
                * 在递归过程中,每个节点都维护者这样一个二维数组;
                * 选择使用后序遍历,因为需要从下到上逐层返回dp数组进行操作;
    """

    def rob( self, root ):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def robTree( iCurNode ):
            if not iCurNode: return [ 0, 0 ]

            leftDp = robTree( iCurNode.left )
            rightDp = robTree( iCurNode.right )

            # -- 不偷 or 偷取 当前节点 --
            dp = [ 0, 0 ]
            dp[ 0 ] = max( leftDp ) + max( rightDp )
            # -- 偷取: dp[1] = 当前值 + 不偷左孩子 + 不偷右孩子 --
            dp[ 1 ] = iCurNode.val + leftDp[ 0 ] + rightDp[ 0 ]

            return dp

        # -- 树的节点数在 [1, 104] 范围内 --
        # -- 0 <= Node.val <= 104 --
        return max( robTree( root ) )
