class Solution( object ):
    """
        给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
        --
        示例
            输入：s = "rabbbit", t = "rabbit"
            输出：3 有 3 种可以从 s 中得到 "rabbit" 的方案。
        --
        目标: 统计并返回在 s 的 子序列 中 t 出现的个数
        1-- dp[ i ][ k ] 表示 以 t[i]结尾的字符串A, 和以 s[k]结尾的字符串B, B中出现A的次数为 dp[i][k]
        2-- 递推公式:
            -- 来考虑 t[i] == or != s[k]的情况 --
                -- 如果 t[i] == s[k] 此时是需要注意的,
                    -- 如示例所示: A=rab, B=rab or B=rabb or B=rabbb B的3种情况均可以构成dp[i][k]
                    -- 所以推导出dp[i][k] 有两种方式, 直接用B or 去掉s[k]
                    -- 所以 当 t[i] == s[k] 时有两种匹配方式: 用s[k]匹配和不用s[k]匹配
                    -- 所以 dp[i][k] = dp[i-1][k-1] + dp[i][ k - 1 ]
                -- 如果 t[i] != s[k] 这种就很简单了
                    -- 直接删掉 s[k], 继续和下一个比较
                    -- 所以 dp[ i ][ k ] = dp[ i ][ k - 1 ]
        3-- 初始化: dp[ 0 ][] 层 和 dp[][ 0 ] 层 ( 对于 dp[][0]层, 当i>0时,由于k==0,所以 t[i]一定不在s[k]中,故均为0 )
        4--遍历顺序:
            -- 其实遍历,按照 先s再t, 或者 先t再s 都行
            -- 为了更好表达, 固定住t, 去删减s中的元素, 我选择先t再s
        5-- 推导递推公式,检验正确性
    """
    def numDistinct( self, s, t ):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n1 = len( s )
        n2 = len( t )
        dp = [ [ 0 for _ in range( n1 ) ] for _ in range( n2 ) ]
        
        if t[ 0 ] == s[ 0 ]: dp[ 0 ][ 0 ] = 1
        # -- 每次当初始化的时候 都要回顾一下dp[i][j]的定义 不要凭感觉初始化  --
        for k in range( 1, n1 ): dp[ 0 ][ k ] = dp[ 0 ][ k - 1 ] + 1 if t[ 0 ] == s[ k ] else dp[ 0 ][ k - 1 ]
        
        for i in range( 1, n2 ):
            for k in range( 1, n1 ):
                if t[ i ] == s[ k ]: dp[ i ][ k ] = dp[ i - 1 ][ k - 1 ] + dp[ i ][ k - 1 ]
                else: dp[ i ][ k ] = dp[ i ][ k - 1 ]
        
        return dp[ -1 ][ -1 ]
                    