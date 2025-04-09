import math


class Solution( object ):
    """
        --[[
            给定正整数 n,找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
        ]]
        -- 本题就不做过多的分析了,和leetcode322兑换零钱的思路完全一致;
        -- ** 特别注意初始化
    """

    def numSquares( self, n ):
        """
        :type n: int
        :rtype: int
        """

        itemN = int( math.sqrt( n ) ) + 1
        packW = n
        inf = n + 1
        
        # -- 初始化 --
        dp = [ inf ] * ( packW + 1 )
        dp[ 0 ] = 0     # -- 递推的数据基础 --
        dp[ 1 ] = 1
        
        for i in range( 1, itemN ):
            for k in range( i * i, packW + 1 ):
                # -- 当i = 2, k = 4时, 使用到dp[ 0 ]的初始值,故需要初始化 --
                dp[ k ] = min( dp[ k ], dp[ k - i * i ] + 1 )
        return dp[ n ] if dp[ n ] < inf else -1


if __name__ == '__main__':
    mN = 12
    print( Solution().numSquares( mN ) )
    