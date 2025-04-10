"""
    --[[
        有n种物品和一个最多能装下重量为w的背包;
        第i种物品最多有 mi 件可用, 每件重量为是wi, 价值为vi;
        求解将哪些物品装入背包可使这些物品重量总和不超过背包容量,且价值总和最大;
    ]]
    [ 注 ]: 每件物品最多有 mi 件可用, 把 mi 件摊开，其实就是一个`01背包`问题, 这样就将`多重背包`问题转成`01背包`问题;
"""


# -- 摊开物品转成01背包的做饭 --
def multipleKnapsack( w, weights, values, quantities ):
    tWeights = []
    tValues  = []
    
    for i in range( 0, len( quantities ) ):
        for k in range( 0, quantities[ i ] ):
            tWeights.append( weights[ i ] )
            tValues.append( values[ i ] )
    n = len( tValues )
    
    # # -- 二维数组的01背包 --
    # dp = [ [ 0 ] * ( w + 1 ) for _ in range( n ) ]
    # for i in range( tWeights[ 0 ], w + 1 ): dp[ 0 ][ i ] = tValues[ 0 ]
    # for i in range( 1, n ):
    #     for k in range( 0, w + 1 ):
    #         if k - tWeights[ i ] >= 0:
    #             dp[ i ][ k ] = max( dp[ i - 1 ][ k ], tValues[ i ] + dp[ i - 1 ][ k - tWeights[ i ] ] )
    #         else:
    #             dp[ i ][ k ] = dp[ i - 1 ][ k ]
    # return dp[ n - 1 ][ w ]
    
    # -- 一维数组01背包 --
    dp = [ 0 ] * ( w + 1 )
    for i in range( 0, n ):
        for k in range( w, tWeights[ i ] - 1, -1 ):
            dp[ k ] = max( dp[ k ], tValues[ i ] + dp[ k - tWeights[ i ] ] )
    return dp[ w ]


# -- 上述代码有个很费的地方: 将物品平铺开转成01背包问题, 看下面代码的优化 --
def multipleKnapsack( w, weights, values, quantities ):
    n = len( quantities )
    dp = [ 0 ] * ( w + 1 )
    for i in range( 0, n ):
        for k in range( w, weights[ i ] - 1, -1 ):
            # -- 在01背包的代码基础上增加遍历个数 --
            # -- 其实就相当于将第i种物品的mi件看做一个整体 --
            for q in range( 1, quantities[ i ] + 1 ):
                if k >= weights[ i ] * q:
                    dp[ k ] = max( dp[ k ], values[ i ] * q + dp[ k - weights[ i ] * q ] )
    return dp[ w ]
    
    
    

if __name__ == '__main__':
    mW = 50
    mValues = [ 60, 100, 120 ]
    mWeights = [ 10, 20, 30 ]
    mQuantities = [ 2, 3, 4 ]
    print( multipleKnapsack( mW, mWeights, mValues, mQuantities ) )
