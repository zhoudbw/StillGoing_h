class Solution( object ):
    """
        --[[
            给定不同面额的硬币 coins 和一个总金额 amount;
            编写一个函数来计算可以凑成总金额所需的最少的硬币个数;如果没有任何一种硬币组合能组成总金额 ,返回 -1;
            你可以认为每种硬币的数量是无限的;
            -- 数据范围:
                1 <= coins.length <= 12
                1 <= coins[i] <= 2e31 - 1
                0 <= amount <= 10e4
        ]]
        -- 方法1: 回溯出所有能够兑成amount的组合, 选择size最小的
        -- 方法2: 动态规划:
        -- * 确定dp数组及其下标含义: dp:从[0,i]中任意取硬币,使之等于k最小硬币数, 即dp( 硬币选择范围, 最小硬币数 );
        -- * 确定递推公式: dp(i, k)的推导来源: dp( i - 1, k ), dp( i, k - coins[ i ] ), 取最小值;
        -- * 如何初始化:
                * 保证计算dp(i,k)时, dp[i-1]以及dp[i][0, k-coins[i])已经被初始化好
                * 首先凑足总金额为0所需钱币的个数一定是0, 那么dp[0] = 0;
                * 考虑到递推公式的特性, dp[j]必须初始化为一个最大的数, 否则就会在min(dp[j - coins[i]] + 1, dp[j])比较的过程中被初始值覆盖;
                * 所以下标非0的元素都是应该是最大值;
        -- * 确定遍历顺序: 求所有情况的最小值, 所以组合数or排列数均不影响最终min保留的数值, 即 先物品再容量 or 先容量再物品 均可;
    """

    def coinChange( self, coins, amount ):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort( reverse = True )
        
        w = amount
        n = len( coins )
        inf = 10e4 + 1

        dp = [ inf ] * ( w + 1 )
        dp[ 0 ] = 0
        
        for i in range( 0, n ):
            for k in range( coins[ i ], w + 1 ):
                # -- 优化 --
                if dp[ k - coins[ i ] ] < inf:
                    dp[ k ] = min( dp[ k ], dp[ k - coins[ i ] ] + 1 )

        return dp[ w ] if dp[ w ] < inf else -1


if __name__ == '__main__':
    mCoins = [1,2,5]
    mAmount = 5
    print( Solution().coinChange( mCoins, mAmount ) )
