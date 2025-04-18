class Solution( object ):

    # -- fool得很呀 --
    def isSubsequence( self, s, t ):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        matchCount = 0  # -- 记录已经匹配到s中多少个字符 --
        tStartIndex = 0  # -- 本轮循环开始,t从第几个开始 --
        for sv in s:
            for i in range( tStartIndex, len( t ) ):
                if t[ i ] == sv:
                    matchCount += 1
                    tStartIndex = i + 1
                    break
        return matchCount == len( s )

    # -- 双指针 --
    def isSubsequence( self, s, t ):
        n1 = len( s )
        if n1 == 0: return True

        sIndex = 0
        for i in range( len( t ) ):
            if t[ i ] == s[ sIndex ]:
                sIndex += 1
                if sIndex == n1: return True
        return False

    # -- 动态规划 --
    # -- 目标: 判断 s 是否是 t 的子序列 --
    # -- 1. dp[i][k]表示以t[k]为结尾字符串A  和以s[k]为结尾的字符串B A包含B的最大字符数 --
    # -- 2. 递推公式, s[i] == t[k]: dp[i][k] = dp[i-1][k-1] + 1
    # --             s[i] != t[k]: 此时应该将t[k]去掉,比较下一个, 所以 dp[i][k] = dp[i][k-1]
    # -- 3. 初始化: dp[ 0 ][] 层 和 dp[][ 0 ] 层
    # -- 4. 遍历顺序: 由于 t是可以动态删除操作的, 所以应该先遍历s,在遍历t
    def isSubsequence( self, s, t ):
        n1 = len( s )
        n2 = len( t )

        if n1 == 0: return True
        if n2 == 0: return False

        dp = [ [ 0 for _ in range( n2 ) ] for _ in range( n1 ) ]

        if s[ 0 ] == t[ 0 ]: dp[ 0 ][ 0 ] = 1
        for k in range( 1, n2 ): dp[ 0 ][ k ] = 1 if s[ 0 ] == t[ k ] else dp[ 0 ][ k - 1 ]
        for i in range( 1, n1 ): dp[ i ][ 0 ] = 1 if s[ i ] == t[ 0 ] else dp[ i - 1 ][ 0 ]

        for i in range( 1, n1 ):
            for k in range( 1, n2 ):
                if s[ i ] == t[ k ]:
                    dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + 1
                else:
                    # -- 两者不相等,说明t[k]结尾字符串中不包含s[i], 所以决定这个值的还是以 t[k-1]即为的字符串是否包含 --
                    # -- 换一种理解,就是此时 t[k] != s[i],需要跳过t[k]( 删掉t[k] ), 继续 t[k+1]的比较 --
                    dp[ i ][ k ] = dp[ i ][ k - 1 ]

        return dp[ -1 ][ -1 ] == n1

        # -- 注意和这题作对比 leetcode1143最长公共子序列` --
