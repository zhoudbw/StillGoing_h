class Solution( object ):
    def climbStairs( self, n ):
        """
        :type n: int
        :rtype: int
        """
        # -- dp[ i ] 表示到达第i个阶梯的方法数 --
        # -- dp[ i ] = dp[i - 1] + dp[ i - 2 ] --
        # -- 根据递推公式,第一项和第二项需要初始化出来 --
        # -- 从递推公式可以看出,遍历顺序一定是从前向后遍历的 --
        if n == 1 or n == 2: return n
        
        dp = [ 0 ] * ( n + 1 )
        dp[ 1 ] = 1
        dp[ 2 ] = 2
        for i in range( 3, n + 1 ):
            dp[ i ] = dp[ i - 1 ] + dp[ i - 2 ]
        return dp[ n ]  # -- 斐波那契数列一样,当前状态依赖前两个状态,可以做空间上的优化 --
        
