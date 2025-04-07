class Solution( object ):
    """
        类似这种题目：给出一个总数，一些物品，问能否凑成这个总数 (凑成总金额的硬币组合数总数)。 这是典型的背包问题！

    
        1. 确定dp数组以及下标的含义:
            -- dp[i][k]：使用 下标为[0, i]的coins[i]能够凑满k（包括k）这么大容量的包，有dp[i][k]种组合方法。
        2. 确定递推公式:
            -- dp[i][k]的来源有两个:不放入coins[i]和放入coins[i]
            -- dp[i][k] = dp[i-1][k] + (1 + dp[i][k-coins[i]]) )
        3. 初始化i=0时的情况
        4. 正常遍历就行,保证递推公式的正确性即可 --
    """
    def change( self, amount, coins ):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        w = amount
        n = len( coins )
        dp = [ 0 ] * ( w + 1 )
        # --
        # -- 这个初始化很重要:::凑成0的一种方式,不放入任何零钱时
        # -- 下面递推公式的时候,考虑的是放入coins[i]+不放入coins[i]
        # -- dp[0]这点的位置,如果不初始化就丢了这种情况 ***
        dp[ 0 ] = 1
        for i in range( 0, n ):
            for k in range( 0, w + 1 ):
                if k - coins[ i ] >= 0:
                    # -- 时刻对标dp数组的含义,根据dp数组的含义去写递推公式
                    # -- 总次数 = 不放入coins[i]的种类数+放入coins[i]的种类数
                    dp[ k ] = dp[ k ] + dp[ k - coins[ i ] ]
        return dp[ w ]
    
    """
        -- 特别地, 上述遍历顺序是否可以调换?
        -- 不可以:
        --  和CompleteKnapsack不一样,从递推公式的角度去分析:
        --  (I)  completeKnapsack: dp[ k ] = max( dp[ k ], dp[ k - weights[ i ] ] + values[ i ] )
        --  (II) dp[ k ] = dp[ k ] + dp[ k - coins[ i ] ]
        -- 在(I)中dp[k]的计算和前者虽然有关系,但是没有做运算,故不影响最终结果;
        -- 但是,在(II)中dp[k]的推导,依赖于同一层dp数组的值,进行运算,如果交换遍历顺序dp[k]所需的dp值不是同一层,error;
    """


if __name__ == '__main__':
    mCoins = [ 1, 2, 5 ]
    mAmount = 5
    print( Solution().change( mAmount, mCoins ) )
