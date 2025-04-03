class Solution( object ):
    """
        -- 01背包问题:
        --      背包的能装下的的重量w
        --      物品有三个属性 重量w, 价值v, 可使用次数t
        -- 
        --  给定一个最多能装重量为w的背包, 以及n件物品( 第i件物品的重量weights[i], 价值values[i] )
        --  *每件物品只能用一次*, 求解将哪些物品装入背包里物品价值总和最大?
    """

    def knapsack01( self, w, n, weights, values ):
        """
        1. 确定dp数组,以及下标含义.
            显然,最大价值受物品和背包容量的影响,需要使用二维数组,需要有两个维度分别表示物品和背包容量; 
            至于dp[i][j]的含义, 这里用i来表示物品,j表示背包容量, i,j调换也是可以的,不影响
            到这里,推导一下dp数组,从而确定dp[i][j]的含义: dp[i][j]表示从下标为[0-i]的物品里任意取,放进容量为j的背包,价值总和最大是多少
        
        2. 确定递推公式:
            对于递推公式,首先要明确有哪些方向可以推导出dp[i][j],即dp[i][j]的来源有哪些???
                由于dp[i-1][j]是任取[0,i-1]的物品放入容量为j的背包内,
                到了dp[i][j]就是将i加入了任取列表,所以dp[i][j]的来源包括: 放入i和不放入i两种情况
                dp[i][j] = max( dp[i-1][j], dp[ i-1 ][ j-weights[i] ] + values[i] )

        3. dp数组如何初始化
        4. 确定遍历顺序
            有两个遍历的维度:物品与背包重量, 先遍历物品还是先遍历背包重量呢?? —— 都可以

        :param w: 背包能装的最大重量
        :param n: 物品数量
        :param weights: n件物品对应的重量
        :param values: n件物品对应的价值
        :return: 最大价值总和
        """
        
        dp = [ [ 0 ] * ( w + 1 ) for _ in range( n ) ]
        # for i in range( 0, w + 1 ): dp[ 0 ][ i ] = ( i >= weights[ 0 ] ) and values[ 0 ] or 0
        for i in range( weights[ 0 ], w + 1 ): dp[ 0 ][ i ] = values[ 0 ]
        print( dp )
        
        for i in range( 1, n ):
            for j in range( 0, w + 1 ):
                # -- 能否放入物品i --
                if j >= weights[ i ]:
                    # -- 能放入,那么在放入和不放入之间取max --
                    dp[ i ][ j ] = max( dp[ i - 1 ][ j ], values[ i ] + dp[ i - 1 ][ j - weights[ i ] ] )
                else:
                    # -- 不能放入,还是上一层的状态( 即,任取[ 0, i - 1 ]物品的价值最大值 ) --
                    dp[ i ][ j ] = dp[ i - 1 ][ j ]
            print( dp )
        return dp[ n - 1 ][ w ]


    def knapsack01( self, w, n, weights, values ):
        """
            对于背包问题其实状态都是可以压缩的:
                在使用二维数组的时候,递推公式：dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
                其实可以发现如果把dp[i - 1]那一层拷贝到dp[i]上,表达式完全可以是：dp[i][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i]);
                与其把dp[i - 1]这一层拷贝到dp[i]上,不如只用一个一维数组了,只用dp[j]（一维数组,也可以理解是一个滚动数组）.
                这就是滚动数组的由来,需要满足的条件是上一层可以重复利用,直接拷贝到当前层.
                
            -- 但是需要特别注意现在的遍历顺序:
                二维dp遍历的时候，背包容量是从小到大，而一维dp遍历的时候，背包是从大到小。
                倒序遍历是为了保证物品i只被放入一次！。但如果一旦正序遍历了，那么物品0就会被重复加入多次！

                因为对于二维dp，dp[i][j]都是通过上一层即dp[i - 1][j]计算而来，本层的dp[i][j]并不会被覆盖！
                而使用一维数组dp是会被覆盖的, 所以dp[j]的求解过程中,容量要倒序遍历
        """

        dp = [ 0 ] * ( w + 1 )
        # -- dp[i][j] = max( dp[i-1][j], dp[i-1][j-weights[i]]+values[i] --
        # -- dp[j] = max( dp[j], dp[j - weights[i]]+values[i] --
        # -- 一定要对标好dp数组的含义 --
        for i in range( 0, n ):
            for j in range( w, weights[ i ] - 1, -1 ):
                # 初始化代码可以放到遍历里面一起操作,因为i==0时,进行初始化,此时只有一个物品,所以只要容积满足,该处的最大价值就是values[0]
                # i>0之后,类比于二维数组,i-1层其实已经初始化好了,从后往前遍历,无重复的再计算出[0,i]个物品可以选取时的最大价值
                # 注意内层循环的边界,以及遍历顺序
                # 截止到weights[i]-1是因为倒序遍历,倒序遍历到的是可以放入物品i的,
                # 而小于weights[i]的是不能够放入物品i的,所以最大价值还是上一层的,即[0,i-1]物品的最大价值,所以这里不需要再继续更新
                dp[ j ] = max( dp[ j ], dp[ j - weights[ i ] ] + values[ i ] )
            print( dp )
        return dp[ w ]
    
        # -- 思考: 是否可以先遍历容量?? --
        


if __name__ == '__main__':
    mW = 4
    mN = 3
    mWeights = [ 1, 3, 4 ]
    mValues = [ 15, 20, 30 ]
    print( Solution().knapsack01( mW, mN, mWeights, mValues ) )
