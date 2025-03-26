class Solution( object ):
    def fib( self, n ):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1: return n
        
        # -- dp[ i ] 表示第i项的斐波那契数 --
        dp = [ 0 ] * ( n + 1 )

        # -- 确定递推公式: dp[ i ] = dp[ i - 1 ] + dp[ i - 2 ] --
        # -- 初始化递推数组 --
        dp[ 0 ] = 0
        dp[ 1 ] = 1
        
        # -- 确定遍历顺序 --
        for i in range( 2, n + 1 ):
            dp[ i ] = dp[ i - 1 ] + dp[ i - 2 ]
            
        return dp[ n ]  # -- 举例推导dp数据组 --

    # -- 空间优化:从上面的代码可以看出,其实只需要存储dp[ i - 1 ]和dp[ i - 2 ]即可 --
    def fib( self, n ):
        if n == 0 or n == 1: return n
        
        dp0, dp1 = 0, 1
        for i in range( 2, n + 1 ):
            dpi = dp0 + dp1
            dp0 = dp1
            dp1 = dpi
        return dp1
        
        
        
        