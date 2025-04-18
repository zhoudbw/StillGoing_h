class Solution( object ):
    """
        给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
        每步 可以删除任意一个字符串中的一个字符。
        -- 方法1 --
        1 求两个字符串的最长公共子序列 A
        2 返回 n1 + n2 - 2 * A
        
        -- 方法2 --
        直接动态规划:
            dp[i][k]：以word1[i]为结尾的字符串A 和以word2[k]结尾的字符串B，想要达到相等 所需要删除元素的最少次数
    """

    def minDistance( self, word1, word2 ):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n1 = len( word1 )
        n2 = len( word2 )
        # -- dp[i][k] 表示以word1[i]结尾的字符串 和 以word2[k]结尾的字符串 的最长公共子序列 --
        dp = [ [ 0 for _ in range( n2 ) ] for _ in range( n1 ) ]

        for k in range( 0, n2 ): dp[ 0 ][ k ] = 1 if word2[ k ] == word1[ 0 ] else dp[ 0 ][ k - 1 ]
        for i in range( 0, n1 ): dp[ i ][ 0 ] = 1 if word1[ i ] == word2[ 0 ] else dp[ i - 1 ][ 0 ]

        for i in range( 1, n1 ):
            for k in range( 1, n2 ):
                if word1[ i ] == word2[ k ]:
                    dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + 1
                else:
                    dp[ i ][ k ] = max( dp[ i - 1 ][ k ], dp[ i ][ k - 1 ] )

        return n1 + n2 - 2 * dp[ -1 ][ -1 ]
