class Solution( object ):
    # -- 暴力:先两层for循环确定两个数组起始位置 然后再来一个循环从两个起始位置开始比较 取得重复子数组的长度 --
    # -- 动态规划 ( 这题需要特别注意一下 ) :
    # --    状态分析
    # --    确定dp数组及其含义: dp[i][k]表示 nums1[ 0, i ]序列 和 nums2[ 0, k ]序列, 其中nums1[i] == nums2[k]时的最长公共数组 --
    # --            这个定义是和巧妙的,只更新 nums1[i] == nums2[k]时, dp[i][k]的值,
    # --            由于是最长重复子数组, 如果出现dp[i][k]的最大值,一定是在两者相等时出现,极大的简化了dp的推导量
    # --    确定递推公式:
    # --        一目了然了: dp[i][k] = dp[i-1][k-1] + 1 ( nums1[i] == nums2[k] )
    # --                  if dp[i][k] > result: result = dp[i][k]   -- 记录最大值 --
    # --    初始化:
    # --        根据dp数组的含义,以及递推公式,初始化第一行和第一列
    # --    遍历顺序:
    # --        从上往下,从左往右即可
    def findLength( self, nums1, nums2 ):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1 = len( nums1 )
        n2 = len( nums2 )

        # -- n1 * n2, n1 行 n2 列 --
        dp = [ [ 0 for _ in range( n2 ) ] for _ in range( n1 ) ]
        result = 0

        for i in range( 0, n2 ):
            if nums2[ i ] == nums1[ 0 ]: dp[ 0 ][ i ] = result = 1
        for i in range( 0, n1 ):
            if nums1[ i ] == nums2[ 0 ]: dp[ i ][ 0 ] = result = 1

        for i in range( 1, n1 ):
            for k in range( 1, n2 ):
                if nums1[ i ] == nums2[ k ]: dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + 1
                if dp[ i ][ k ] > result: result = dp[ i ][ k ]

        return result

# -- 很显然上述代码可以优化为一维 --
# -- 因为dp数组的推导,只依赖于上一层dp的值 --


if __name__ == '__main__':
    # mNums1 = [ 0, 0, 0, 0, 1 ]
    # mNums2 = [ 1, 0, 0, 0, 0 ]
    mNums1 = [ 1, 0, 0, 0, 1 ]
    mNums2 = [ 1, 0, 0, 1, 1 ]
    print( Solution().findLength( mNums1, mNums2 ) )
