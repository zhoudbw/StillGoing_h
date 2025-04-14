class Solution( object ):
    """
        --[[
            给定一个数组 prices,它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格;
            你只能选择 某一天 买入这只股票,并选择在 未来的某一个不同的日子 卖出该股票;
            设计一个算法来计算你所能获取的最大利润;
            返回你可以从这笔交易中获取的最大利润;如果你不能获取任何利润,返回 0 ;
            --
            注意: 根据题意,只有一次买入和售出的交易
        ]]
        
        -- conclusion --
        --  * 确定变化因素的状态:
                * 比如本题中的 股票有两种状态: 买入 or 卖出
                
        --  * 确定dp数组及其下标:
                * dp[i][0]表示第i天未持有股票的最高利润
                * dp[i][1]表示第i天持有股票的最高利润
                
        --  * 确定递推公式:
                * dp[i][0] 有两个来源:
                    * i-1天时未持有   * i天的时卖出
                * dp[i][1] 有两个来源:
                    * i-1天时持有     * i天的时买入
                
                dp[i][0] = max( dp[i-1][0], prices[i] + dp[i-1][1] )
                dp[i][1] = max( dp[i-1][1], -prices[i]
        
        -- * 初始化:
                * 根据递推公式, 初始化dp[0]即可
        
        -- * 遍历顺序:
                * 根据递推公式, 从前往后即可
        
        -- * 实例推导dp数组,检测分析的正确性
                        
    """

    def maxProfit( self, prices ):
        n = len( prices )
        dp = [ [ 0, 0 ] for _ in range( n ) ]

        dp[ 0 ][ 0 ] = 0
        dp[ 0 ][ 1 ] = -prices[ 0 ]

        for i in range( 1, n ):
            dp[ i ][ 0 ] = max( dp[ i - 1 ][ 0 ], prices[ i ] + dp[ i - 1 ][ 1 ] )
            dp[ i ][ 1 ] = max( dp[ i - 1 ][ 1 ], -prices[ i ] )

        return max( dp[ -1 ][ 0 ], dp[ -1 ][ 1 ] )

    # -- 从递推公式可以看出,dp[i]只是依赖于dp[i - 1]的状态, 所以只需要记录前一天的状态即可 --
    def maxProfit( self, prices ):
        n = len( prices )
        dp = [ 0, -prices[ 0 ] ]

        for i in range( 1, n ):
            dp[ 0 ] = max( dp[ 0 ], prices[ i ] + dp[ 1 ] )
            dp[ 1 ] = max( dp[ 1 ], -prices[ i ] )

        return max( dp )

    # -- 贪心 --
    # -- 取左边的最小值, 和作差的最大值 --
    def maxProfit( self, prices ):
        n = len( prices )
        minValue = float( 'inf' )
        maxValue = 0

        for i in range( 0, n ):
            minValue = min( minValue, prices[ i ] )
            maxValue = max( maxValue, prices[ i ] - minValue )
        return maxValue
