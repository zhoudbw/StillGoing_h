class Solution( object ):
    """
        --[[
            给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
            子数组是数组中的一个连续部分。
        ]]
        动态规划:
            确定dp数组及其含义: dp[i]表示以 nums[i]结尾的连续子数组的最大和
            确定递推公式: dp[i] = max( dp[i-1] + nums[i], nums[i] )
                * 如果加入nums[i]之后,这段数组开始变小,根据dp数组的含义,就需要从nums[i]开始重新计算
                * 比如说, 如果dp[i-1] + nums[i]变小, 那么dp[i-2] + nums[i], dp[i-3] +nums[i] 都是变小,所以从nums[i]开始重新计算\
                * 需要特别注意: 递推完成之后,返回的是这其中最大的值,而不是最后dp[-1]
                    dp[i]的定义: dp[i]表示以 nums[i]结尾的连续子数组的最大和
                    所以要找最大的连续子序列,应该找每一个i为终点的连续最大子序列, 所以在递推公式的时候,可以直接选出最大的dp[i]
            初始化: dp[ 0 ]
            遍历顺序: 从前往后
    """

    def maxSubArray( self, nums ):
        """
        :type nums: List[int]
        :rtype: int
        """
        n       = len( nums )
        dp      = [ 0 for _ in range( n ) ]
        dp[ 0 ] = result = nums[ 0 ]

        for i in range( 1, n ):
            dp[ i ] = max( nums[ i ] + dp[ i - 1 ], nums[ i ] )
            if dp[ i ] > result: result = dp[ i ]

        return result


if __name__ == '__main__':
    mNums = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
    print( Solution().maxSubArray( mNums ) )
