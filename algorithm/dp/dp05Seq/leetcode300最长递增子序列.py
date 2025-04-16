class Solution( object ):
    """
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
        子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
        例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
        
        --
        状态分析: 对于每个数,有两种选择: 加入最长子序列 or 不加入最长子序列
        dp数组及其含义:
            dp[i][0]表示[0,i]这段序列中,加入最长严格递增子序列的最大长度
            dp[i][1]表示[0,i]这段序列中,不加入最长严格递增子序列的最大长度
        确定递推公式:
            dp[0, i-1][0,1]已知, 求dp[i][0,1]
                * 需要从0,遍历到i-1, 即
                if nums[i] > nums[k]:
                    dp[i][0] = max( dp[i][0], dp[k][0] + 1 )
                else:
                    dp[i][1] = max( dp[i][1], dp[k][0], dp[k][1] )
        初始化:
            对于加入序列的位置,全部初始化为 1
            对于未加入序列的位置,全部初始化为 0
        遍历顺序:
            按照递推公式, 从前往后遍历即可
    """

    def lengthOfLIS( self, nums ):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len( nums )
        dp = [ [ 1, 0 ] for _ in range( n ) ]

        for i in range( 1, n ):
            for k in range( 0, i ):
                if nums[ i ] > nums[ k ]:
                    # -- 这里需要特别注意一下, 由于nums[i] > nums[k]所以,一定是在加入了k的序列中+1 --
                    dp[ i ][ 0 ] = max( dp[ i ][ 0 ], dp[ k ][ 0 ] + 1 )
                else:
                    dp[ i ][ 1 ] = max( dp[ i ][ 1 ], dp[ k ][ 0 ], dp[ k ][ 1 ] )

        return max( dp[ - 1 ] )

    # -- 换一种定义dp的做法 --
    # -- dp[i] 表示[0,i]序列的最长严格单调递增序列的长度 --
    # -- 初始化: 根据dp数组的含义,每个位置初始化为1
    def lengthOfLIS( self, nums ):
        n = len( nums )
        dp = [ 1 for _ in range( n ) ]

        result = 1
        for i in range( 1, n ):
            for k in range( 0, i ):
                if nums[ i ] > nums[ k ]:
                    dp[ i ] = max( dp[ i ], dp[ k ] + 1 )
            # -- 对于 nums[i] <= nums[k]的情况是没有改变dp[i]位置的值的 --
            # -- 但是记录了过程中的最大值,最终返回的就是最长严格递增子序列的值 --
            if dp[ i ] > result: result = dp[ i ]
            
        return result


if __name__ == '__main__':
    mNums = [ 4, 10, 4, 3, 8, 9 ]
    print( Solution().lengthOfLIS( mNums ) )
