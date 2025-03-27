class Solution( object ):
    def uniquePaths( self, m, n ):
        """
        1 <= m, n <= 100
        :type m: int
        :type n: int
        :rtype: int
        """
        # - start = ( 0, 0 ), finish = ( m - 1, n - 1 ) --
        # -- dp[i][k] 表示走到格点(i,k)处有多少种走法 --
        # -- dp[i][k] = dp[i-1][k] + dp[i][k-1], dp[i][k]可以从改点的正上方一格或改点的正左方一个得到 --
        # -- 初始化dp数组,显然需要初始化第0行和第0列,防止dp计算越界 --
        # -- 遍历顺序,从左到右一层一层遍历就可以,dp计算需要前面值的状态已知 --

        dp = [ [ 0 ] * n for _ in range( m ) ]
        for i in range( m ): dp[ i ][ 0 ] = 1
        for i in range( n ): dp[ 0 ][ i ] = 1

        for i in range( 1, m ):
            for k in range( 1, n ):
                dp[ i ][ k ] = dp[ i - 1 ][ k ] + dp[ i ][ k - 1 ]
        return dp[ m - 1 ][ n - 1 ]

    # -- 将dp数组优化成一维数组 --
    # -- dp[i][k] = dp[i-1][k] + dp[i][k-1], 其实在dp[i][k]没有更新前,此时的dp[i][k]就是dp[i][k-1]
    def uniquePaths( self, m, n ):

        dp = [ 1 ] * n
        for i in range( 1, m ):
            for k in range( 1, n ):
                dp[ k ] = dp[ k ] + dp[ k - 1 ]
        return dp[ n - 1 ]
   