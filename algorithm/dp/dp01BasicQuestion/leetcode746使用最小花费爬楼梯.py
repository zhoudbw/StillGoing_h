class Solution( object ):
    
    # -- 明确一下: 请你计算并返回达到楼梯顶部的最低花费。 --
    # -- 到达楼梯顶部,是指到达 len( cost ) 位置,这样才算是到达了顶部 --
    def minCostClimbingStairs( self, cost ):
        """
        :type cost: List[int]
        :rtype: int
        """
        # -- dp[ i ]:在第i阶台阶的最小消耗 --
        # -- 由于每次可以选择跳1阶或者两阶,所以到达第i阶,就是从i-1阶或i-2阶到达,
        #    那么dp[ i - 1 ] = min( dp[ i - 1 ] + val[ i - 1 ], dp[ i - 2 ] + val[ i - 2 ] ) --
        # -- 根据递推公式,显然需要初始化dp[0]和dp[1]才可以防止数组操作报错 --
        # -- 显然,根据递推公式,遍历顺序从前往后 --
        n = len( cost )     # -- 注,由于下标从0开始,从0~n有n+1项 --
        if n == 0 or n == 1: return 0
        
        dp = [ 0 ] * ( n + 1 )
        for i in range( 2, n + 1 ):
            dp[ i ] = min( dp[ i - 1 ] + cost[ i - 1 ], dp[ i - 2 ] + cost[ i - 2 ] )
        return dp[ n ]

    # -- 优化空间,只存储dpi需要的状态 --
    def minCostClimbingStairs( self, cost ):
        dp0 = 0
        dp1 = 0
        for i in range( 2, len( cost ) + 1 ):
            dpi = min( dp1 + cost[ i - 1 ], dp0 + cost[ i - 2 ] )
            dp0 = dp1
            dp1 = dpi
        return dp1
    
    
"""
补充： 如果按照 第一步是花费的，最后一步不花费，那么代码是这么写的

class Solution:
    def minCostClimbingStairs( self, cost: List[ int ] ) -> int:
        dp = [ 0 ] * len( cost )
        # -- 第一步有花费 --
        dp[ 0 ] = cost[ 0 ]
        dp[ 1 ] = cost[ 1 ]
        for i in range( 2, len( cost ) ):
            dp[ i ] = min( dp[ i - 1 ], dp[ i - 2 ] ) + cost[ i ]
        
        # -- 注意最后一步不用花费，所以取倒数第一步，第二步的最少值 --
        # -- 特别注意 --
        return min( dp[ -1 ], dp[ -2 ] )
        
"""



