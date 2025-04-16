class Solution( object ):
    def findLengthOfLCIS( self, nums ):
        """
        :type nums: List[int]
        :rtype: int
        """
        # -- 本题相对于 `leetcode300最长递增子序列`要容易喝多,dp数组定义为一维即可 --
        # -- dp[i] 表示以下标i为结尾的连续递增的子序列长度 --
        n = len( nums )
        dp = [ 1 for _ in range( n ) ]

        result = 1
        for i in range( 1, n ):
            if nums[ i ] > nums[ i - 1 ]: dp[ i ] = dp[ i - 1 ] + 1
            if dp[ i ] > result: result = dp[ i ]
        return result
