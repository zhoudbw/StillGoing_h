class Solution( object ):
    """
        给你一个整数数组 prices 和一个整数 k ,其中 prices[i] 是某支给定的股票在第 i 天的价格.
        设计一个算法来计算你所能获取的最大利润.你最多可以完成 k 笔交易.也就是说,你最多可以买 k 次,卖 k 次.
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
        --
        本题当做 `leetcode123买卖股票的最佳时机III`的第二问接着做  ( 区别 最多完成k笔交易 )
        
        * 状态分析:
            0 没有操作的状态
            1 第一次持有股票
            2 第一次不持有股票
            3 第二次持有股票
            4 第二次不持有股票
            ...
            共 2 * k + 1 个状态
        * 确定dp数组及其下标含义:
            dp[i][j] 第i天时,处于j状态的最高利润
        * 确定递推公式:
            dp[i][0] 始终为0,保持默认值即可
            dp[ i ][ 1 ] = max( dp[ i - 1 ][ 1 ], dp[ i - 1 ][ 0 ] - prices[ i ] )
            dp[ i ][ 2 ] = max( dp[ i - 1 ][ 2 ], dp[ i - 1 ][ 1 ] + prices[ i ] )
            dp[ i ][ 3 ] = max( dp[ i - 1 ][ 3 ], dp[ i - 1 ][ 2 ] - prices[ i ] )
            dp[ i ][ 4 ] = max( dp[ i - 1 ][ 4 ], dp[ i - 1 ][ 3 ] + prices[ i ] )
            ...
            可以发现,对于状态j,
            dp[ i ][ j为奇数 ] = max( dp[ i - 1 ][ j ], dp[ i - 1 ][ j - 1 ] - prices[ i ] )
            dp[ i ][ j为偶数 ] = max( dp[ i - 1 ][ j ], dp[ i - 1 ][ j - 1 ] + prices[ i ] )
        * 确定初始化值:
            初始化和`leetcode123买卖股票的最佳时机III`一致
        * 确定遍历顺序:
            遍历顺序和`leetcode123买卖股票的最佳时机III`一致
        * 实例检查dp数组的正确性
    """

    def maxProfit( self, k, prices ):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len( prices )
        dp = [ [ 0 for _ in range( 2 * k + 1 ) ] for _ in range( n ) ]

        for j in range( 1, 2 * k + 1, 2 ): dp[ 0 ][ j ] = -prices[ 0 ]

        for i in range( 1, n ):
            for j in range( 1, 2 * k + 1, 2 ):
                dp[ i ][ j ] = max( dp[ i - 1 ][ j ], dp[ i - 1 ][ j - 1 ] - prices[ i ] )
                dp[ i ][ j + 1 ] = max( dp[ i - 1 ][ j + 1 ], dp[ i - 1 ][ j ] + prices[ i ] )

        return dp[ -1 ][ 2 * k ]

    # -- 空间优化 --
    def maxProfit( self, k, prices ):
        n = len( prices )
        dp = [ 0 for _ in range( 2 * k + 1 ) ]

        for j in range( 1, 2 * k + 1, 2 ): dp[ j ] = -prices[ 0 ]

        for i in range( 1, n ):
            for j in range( 1, 2 * k + 1, 2 ):
                dp[ j ] = max( dp[ j ], dp[ j - 1 ] - prices[ i ] )
                dp[ j + 1 ] = max( dp[ j + 1 ], dp[ j ] + prices[ i ] )

        return dp[ 2 * k ]

    # -- 换一种定义dp数组的方式:
    #   dp[i][k][0] 表示 第i天时,第k次持有股票的最高金额
    #   dp[i][k][1] 表示 第i天时,第k次不持有股票的最高金额
    #   dp[i][k][0] = max( dp[i-1][k][0], dp[i-1][k-1][1] - prices[i] )
    #   dp[i][k][1] = max( dp[i-1][k][1], dp[i-1][k][0] + prices[i] )
    def maxProfit( self, k, prices ):
        n = len( prices )
        dp = [ [ [ 0, 0 ] for _ in range( k + 1 ) ] for _ in range( n ) ]

        for p in range( 1, k + 1 ): dp[ 0 ][ p ][ 0 ] = -prices[ 0 ]

        for i in range( 1, n ):
            for p in range( 1, k + 1 ):
                dp[ i ][ p ][ 0 ] = max( dp[ i - 1 ][ p ][ 0 ], dp[ i - 1 ][ p - 1 ][ 1 ] - prices[ i ] )
                dp[ i ][ p ][ 1 ] = max( dp[ i - 1 ][ p ][ 1 ], dp[ i - 1 ][ p ][ 0 ] + prices[ i ] )

        return max( dp[ n - 1 ][ k ] )
