class Solution( object ):
    """
        给你一个整数数组prices,其中prices[i]表示某支股票第i天的价格;
        在每一天,你可以决定是否购买 和/或 出售股票;
        你在任何时候最多只能持有一股股票;你也可以先购买,然后在同一天出售;
        返回你能获得的最大利润;
    --
        动态规划 ( 本题和`leetcode121买卖股票的最佳时机`的区别就在于交易次数, 这体现在递推公式中 ) :
            * dp[i][0]表示第i天没有持有股票的最高收益
            * dp[i][1]表示第i天持有股票的最高收益
            -- 上述两种情况就已经涵盖了出现最高收益的情况 --
            * dp[i][0] 的来源: i-1天时未持有股票; i天时卖出股票
            * dp[i][1] 的来源: i-1天时持有股票; i天买入股票
            -- 由于存在多次交易,递推公式不同于`leetcode121买卖股票的最佳时机` --
                * dp[i][0] = max( dp[ i - 1 ][ 0 ], dp[ i - 1 ][ 1 ] + prices[ i ] )
                * dp[i][1] = max( dp[ i - 1 ][ 1 ], dp[ i - 1 ][ 0 ] - prices[ i ] )
        --这正是因为本题的股票可以买卖多次;
        -- 所以买入股票的时候,可能会有之前买卖的利润即:dp[i - 1][1],所以dp[i - 1][1] - prices[i];
    """

    def maxProfit( self, prices ):
        n = len( prices )

        dp = [ [ 0, 0 ] for _ in range( n ) ]
        dp[ 0 ][ 0 ] = 0
        dp[ 0 ][ 1 ] = -prices[ 0 ]

        for i in range( 1, n ):
            dp[ i ][ 0 ] = max( dp[ i - 1 ][ 0 ], dp[ i - 1 ][ 1 ] + prices[ i ] )
            dp[ i ][ 1 ] = max( dp[ i - 1 ][ 1 ], dp[ i - 1 ][ 0 ] - prices[ i ] )

        return max( dp[ -1 ] )
    

    def maxProfit( self, prices ):
        n = len( prices )

        dp = [ 0, -prices[ 0 ] ]

        for i in range( 1, n ):
            dp[ 0 ] = max( dp[ 0 ], dp[ 1 ] + prices[ i ] )
            dp[ 1 ] = max( dp[ 1 ], dp[ 0 ] - prices[ i ] )

        return max( dp )
