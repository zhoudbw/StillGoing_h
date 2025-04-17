class Solution( object ):
    """
        动态规划:
            dp数组及其含义: dp[i][k] 表示以text1[i]结尾的字符串 和 以text2[k]结尾的字符串 的最长公共子序列
            确定递推公式:
                if text1[ i ] == text2[ k ]:
                    dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + 1
                * 这一点很容易想通, 比如 abcde,abc这两个字符串,由于dp[i][k]表示以i,k结尾的字符串的最长公共子序列长度
                * 比如 abcde, abc  ( ..a, ..a ) ( ..b, ..b ) ( ..c, ..c ) 在text1[ i ] == text2[ k ]时更新,就能保证正确性
                else:
                    dp[ i ][ k ] = max( 以i-1结尾的字符串和以k结尾的字符串, 以i结尾的字符串和以k-1结尾的字符串 )
            初始化: 初始化第一行和第一列
            遍历顺序: 从前往后 从上往下
            推导递推公式检验正确性
    """

    def longestCommonSubsequence( self, text1, text2 ):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n1 = len( text1 )
        n2 = len( text2 )
        dp = [ [ 0 for _ in range( n1 ) ] for _ in range( n2 ) ]

        for k in range( 0, n1 ):
            if text1.find( text2[ 0 ], 0, k + 1 ) != -1: dp[ 0 ][ k ] = 1
        for i in range( 0, n2 ):
            if text2.find( text1[ 0 ], 0, i + 1 ) != -1: dp[ i ][ 0 ] = 1

        for i in range( 1, n2 ):
            for k in range( 1, n1 ):
                if text2[ i ] == text1[ k ]:
                    dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + 1
                else:
                    dp[ i ][ k ] = max( dp[ i - 1 ][ k ], dp[ i ][ k - 1 ] )

        return dp[ -1 ][ -1 ]
