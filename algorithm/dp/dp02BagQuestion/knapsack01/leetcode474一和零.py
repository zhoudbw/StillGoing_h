class Solution( object ):
    """
        --[[
            给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
            请你找出并返回 strs 的最大子集的长度,该子集中 最多 有 m 个 0 和 n 个 1 。
            如果 x 的所有元素也是 y 的元素,集合 x 是集合 y 的 子集 。
        ]]
        -- 方法1: 回溯找到所有集合的组合,校验是否满足上述条件,返回元素最多的子集长度 --
        -- 方法2: 动态规划 ( 从方法1可以知道,题目隐含着`集合中任意取`,定式思维就可以想想背包 ) --
        --  特别注意的,这个背包维度的背包, 即 m个0 和 n个1 两个维度 --
        --  字符串的zeroNum和oneNum相当于物品的重量, 字符串自己的本身的个数相当于物品的价值( 即, 1 )
        --      确定dp数组及其下标含义: dp[i][m][n]表示任取[0,i]个物品,装入m个0,n个1的背包的最大子集长度 --
        --      确定递推公式:
        --          dp[i][m][n]的来源: 两个来源 放进strs[i]和不放入strs[i]的最大长度
                    则: dp[i][m][n] = max( dp[i][m][n], dp [i-1] [m-strs[i]中0个个数] [n-strs[i]中1的个数] + 1 )
        --      初始化dp数组:
                    因为物品价值不会是负数,初始为0,保证递推的时候dp[i][k]不会被初始值覆盖
        --      遍历顺序,显然从上到下,从左到右即可 --
    """

    def findMaxForm( self, strs, m, n ):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def getZeroOneCount( iStr ):
            iZeroCount, iOneCount = 0, 0
            if len( iStr ) > 0:
                for c in iStr:
                    if c == '0':
                        iZeroCount += 1
                    elif c == '1':
                        iOneCount += 1

            return iZeroCount, iOneCount

        # -- 动态规划 --
        
        dp = [ [ [ 0 ] * (n + 1) for _ in range( m + 1 ) ] for _ in range( len( strs ) + 1 ) ]
        
        # -- 初始化 ( 集合中最多 有 m 个 0 和 n 个 1 ) --
        # --    所以: 当0的数量和1的数量 都容得下0号字符串时,将dp数组的相应位置初始化为1,即当前的子集数量为1 --
        # --    要始终对标着dp数组的含义 --
        zeroCount, oneCount = getZeroOneCount( strs[ 0 ] )
        for i in range( zeroCount, m + 1 ):
            for k in range( oneCount, n + 1 ):
                dp[ 0 ][ i ][ k ] = 1
        
        for i in range( 1, len( strs ) ):
            zeroCount, oneCount = getZeroOneCount( strs[ i ] )
            for p in range( 0, m + 1 ):
                for q in range( 0, n + 1 ):
                    if p >= zeroCount and q >= oneCount:
                        dp[ i ][ p ][ q ] = max( dp[ i - 1 ][ p ][ q ],  dp[ i - 1 ][ p - zeroCount ][ q - oneCount ] + 1 )
                    else:
                        dp[ i ][ p ][ q ] = dp[ i - 1 ][ p ][ q ]
        
        return dp[ len( strs ) - 1 ][ m ][ n ]

    
    """
        -- 压缩dp --
        dp[i][k]表示,i个0,k个1的容量背包, 能装下的strs的最大子集长度
    """
    def findMaxForm( self, strs, m, n ):
        def getZeroOneCount( iStr ):
            iZeroCount, iOneCount = 0, 0
            if len( iStr ) > 0:
                for c in iStr:
                    if c == '0':
                        iZeroCount += 1
                    elif c == '1':
                        iOneCount += 1

            return iZeroCount, iOneCount
        
        dp = [ [ 0 ] * ( n + 1 ) for _ in range( m + 1 ) ]
        for i in range( len( strs ) ):
            zeroCount, oneCount = getZeroOneCount( strs[ i ] )
            for p in range( m, zeroCount - 1, - 1):
                for q in range( n, oneCount - 1, - 1 ):
                    dp[ p ][ q ] = max( dp[ p ][ q ], dp[ p - zeroCount ][ q - oneCount ] + 1 )
        return dp[ m ][ n ]
    

if __name__ == '__main__':
    mStrs = [ "10", "0001", "111001", "1", "0" ]
    mM = 5
    mN = 3
    print( Solution().findMaxForm( mStrs, mM, mN ) )
