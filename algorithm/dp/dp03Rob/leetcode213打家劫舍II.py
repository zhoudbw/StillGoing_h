class Solution( object ):
    """
        --[[
            你是一个专业的小偷,计划偷窃沿街的房屋,每间房内都藏有一定的现金;这个地方所有的房屋都围成一圈,
            这意味着第一个房屋和最后一个房屋是紧挨着的;同时,相邻的房屋装有相互连通的防盗系统,
            如果两间相邻的房屋在同一晚上被小偷闯入,系统会自动报警 ;
            给定一个代表每个房屋存放金额的非负整数数组,计算你 在不触动警报装置的情况下,今晚能够偷窃到的最高金额;
            
            1 <= nums.length <= 100
            0 <= nums[i] <= 1000
        ]]
        -- 本题和 `leetcode198打家劫舍` 唯一区别就是成环
        -- 分析:
        --  首尾成环,
            * 偷第0号房间,最后一个房间就不能偷; 偷取范围 [0,n-2]
            * 不偷第0号房间,最后一个房间就能偷; 偷取范围 [1,n-1]
            ( 全集 )
    """

    def rob( self, nums ):

        def robRange( iNums ):
            iN = len( iNums )

            # -- dp[i][0]表示不偷 i号房间, [0,i]号房间偷到的最高金额 --
            # -- dp[i][1]表示偷 i号房间, [0,i]号房间偷到的最高金额 --
            dp = [ [ 0, 0 ] for _ in range( iN ) ]

            # -- i号房间 偷or不偷 取决于 i-1号房间, 以及 最后一个房间时还需要考虑0号房间 --
            dp[ 0 ][ 0 ] = 0
            dp[ 0 ][ 1 ] = iNums[ 0 ]

            for i in range( 1, iN ):
                dp[ i ][ 0 ] = max( dp[ i - 1 ][ 0 ], dp[ i - 1 ][ 1 ] )
                dp[ i ][ 1 ] = iNums[ i ] + dp[ i - 1 ][ 0 ]

            return max( dp[ iN - 1 ][ 0 ], dp[ iN - 1 ][ 1 ] )

        # -- 由于涉及到数组的拆分,需要确保拆分有意义 --
        if len( nums ) < 3: return max( nums )
        return max( robRange( nums[ 0:-1 ] ), robRange( nums[ 1: ] ) )

    def rob( self, nums ):

        def robRange( iNums ):
            # -- dp[i]表示[0,i]偷到的最高金额 --
            n = len( iNums )
            dp = [ 0 ] * n

            # -- dp[0,i-1]已知,dp[i]的推导来源: 偷i号房间or不偷i号房间 --
            # -- dp[i] = max( nums[i]+dp[i-2], dp[i-1] )
            dp[ 0 ] = iNums[ 0 ]
            dp[ 1 ] = max( iNums[ 0 ], iNums[ 1 ] )
            for i in range( 2, n ):
                dp[ i ] = max( iNums[ i ] + dp[ i - 2 ], dp[ i - 1 ] )

            return dp[ -1 ]

        if len( nums ) <= 3: return max( nums )
        return max( robRange( nums[ :-1 ] ), robRange( nums[ 1: ] ) )


if __name__ == '__main__':
    mNums = [ 1, 2, 3, 1 ]
    print( Solution().rob( mNums ) )
