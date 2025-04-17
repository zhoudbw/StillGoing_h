class Solution( object ):
    """
        --[[
            在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
            现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足：
                 nums1[i] == nums2[j]
                且绘制的直线不与任何其他连线（非水平线）相交。
            请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
            以这种方法绘制线条，并返回可以绘制的最大连线数。
        ]]
        本题其实就是求最长公共子序列
    """

    def maxUncrossedLines( self, nums1, nums2 ):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1 = len( nums1 )
        n2 = len( nums2 )
        dp = [ [ 0 for _ in range( n1 ) ] for _ in range( n2 ) ]

        dp[ 0 ][ 0 ] = 1 if nums1[ 0 ] == nums2[ 0 ] else 0
        for k in range( 1, n1 ):
            dp[ 0 ][ k ] = 1 if nums1[ k ] == nums2[ 0 ] else dp[ 0 ][ k - 1 ]
        for i in range( 1, n2 ):
            dp[ i ][ 0 ] = 1 if nums2[ i ] == nums1[ 0 ] else dp[ i - 1 ][ 0 ]
            
        for i in range( 1, n2 ):
            for k in range( 1, n1 ):
                if nums2[ i ] == nums1[ k ]: dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + 1
                else: dp[ i ][ k ] = max( dp[ i - 1 ][ k ], dp[ i ][ k - 1 ] )
        
        return dp[ -1 ][ -1 ]
