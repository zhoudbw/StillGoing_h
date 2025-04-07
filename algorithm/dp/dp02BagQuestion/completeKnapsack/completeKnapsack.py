"""
    -- 完全背包 --
        -- 有N件物品和一个最多能背重量为w的背包.第i件物品的重量是weights[i],得到的价值是values[i].
        -- 每件物品都有无限个( 也就是可以放入背包多次 ),求解将哪些物品装入背包里物品价值总和最大.
        
    完全背包和01背包问题唯一不同的地方就是,每种物品有无限件.
    
    -- 完全背包的递推过程 --
        dp[i][k]表示从下标为[0-i]的物品,每个物品可以取无限次,放进容量为k的背包,价值总和最大是多少.
        --
        求取 dp[i][k] 有两种情况： 放物品i 还是不放物品i. 抽象化如下:
            -- 不放物品i：背包容量为k,里面不放物品i的最大价值是dp[i - 1][k].
            -- 放物品i：背包空出物品i的容量后,背包容量为k - weight[i],
                dp[i][k - weight[i]] 为背包容量为k - weight[i]且不放物品i的最大价值,
                那么dp[i][k - weight[i]] + value[i] ( 物品i的价值 ),就是背包放物品i得到的最大价值
                
        递推公式： dp[i][k] = max(dp[i - 1][k], dp[i][k - weight[i]] + value[i]);
        
    -- ( 注意,`完全背包二维dp数组`和`01背包二维dp数组`,以及`递推公式`的区别,
        01背包中是 dp[i - 1][k - weight[i]] + value[i]) ) --
"""


def completeKnapsack( w, n, weights, values ):
    
    dp = [ [ 0 ] * ( w + 1 ) for _ in range( n ) ]
    
    # -- dp数组初始化:
    # -- 二维数组的最上行 和 最左列一定要初始化,这是递推公式推导的基础
    # --    1. 根据递推公式i-1行需要初始化( 即i=0需要初始化 ),由于物品有无限个,所以最大价值为w能够装下的最多物品数*价值
    # -- 再看递推公式,可以看出dp[i][j] 是由上方和左方数值推导出来了,那么其他下标初始为任意数值都可以因为都会被覆盖,无需特别初始化
    # for i in range( weights[ 0 ], w + 1 ): dp[ 0 ][ i ] = ( i // weights[ 0 ] ) * values[ 0 ]
    
    # -- 另一种初始化的方法: 如果能放下就一直装物品0 ( 初始化的时候一定要紧紧抓住dp数组的含义 ):
    for k in range( weights[ 0 ], w + 1 ): dp[ 0 ][ k ] = dp[ 0 ][ k - weights[ 0 ] ] + values[ 0 ]
    
    for i in range( 1, n ):
        for k in range( 0, w + 1 ):
            if k >= weights[ i ]:
                # -- 能够放下i号物品
                dp[ i ][ k ] = max( dp[ i - 1 ][ k ], dp[ i ][ k - weights[ i ] ] + values[ i ] )
            else:
                # -- 不能放下i号物品
                dp[ i ][ k ] = dp[ i - 1 ][ k ]
    return dp[ n - 1 ][ w ]


def completeKnapsack( w, n, weights, values ):
    
    dp = [ 0 ] * ( w + 1 )
    # -- 初始化在下面的递推中完全可以涵盖
    # for k in range( weights[ 0 ], w + 1 ): dp[ k ] = values[ 0 ] + dp[ 0 ][ k - weights[ 0 ] ]
    
    # -- 注: 在01背包中,一维dp遍历顺序必须是先物品再容量;
    # -- 而完全背包中的一维dp遍历顺序没有影响,因为两种遍历方式都是通过dp[k-weight[i]]递推出来;
    for i in range( 0, n ):
        # -- 由于dp[k]需要由dp[k-weights[i]递推出来,所以这里的遍历和01背包就有所不同
        """
            对于纯完全背包问题,其for循环的先后循环是可以颠倒的！
            但如果题目稍稍有点变化，就会体现在遍历顺序上.
            如果问装满背包有几种方式的话？ 那么两个for循环的先后顺序就有很大区别了, 后续做题的时候需要特别注意。
        """
        
        for k in range( 0, w + 1 ):
            if k - weights[ i ] >= 0: dp[ k ] = max( dp[ k ], dp[ k - weights[ i ] ] + values[ i ] )
    return dp[ w ]


"""
    -- 注: 先遍历物品 or 先遍历重量均可
"""
        


if __name__ == '__main__':
    mW, mN = map( int, input().split() )
    mWeights = []
    mValues = []
    for _ in range( mN ):
        iw, iv = map( int, input().split() )
        mWeights.append( iw )
        mValues.append( iv )
    
    # -- 测试用例
    #       mW = 4
    #       mN = 3
    #       mWeights = [ 1, 3, 4 ]
    #       mValues = [ 15, 20, 30 ]
    print( completeKnapsack( mW, mN, mWeights, mValues ) )

    