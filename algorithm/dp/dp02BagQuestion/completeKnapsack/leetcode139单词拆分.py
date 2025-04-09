class Solution( object ):
    """
        --[[
            给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
            注意：不要求字典中出现的单词全部都使用,并且字典中的单词可以重复使用。
        ]]
        -- 方法1: 枚举分割所有字符串,判断是否在字典里出现过;
        -- 方法2: 动态规划
            * 单词就是物品,字符串s就是背包,单词能否组成字符串s,就是问物品能不能把背包装满;
            * 拆分时可以重复使用字典中的单词,说明就是一个完全背包;
                * 确定dp数组和下标的含义: dp[k] 字符串长度为k可以拆分为一个或多个在字典中出现的单词的状态( true or false );
                * 确定递推公式: wordDict[i]是否放入背包中, 设wordDict[i]的长度为 x :
                    * 如果放入: dp[ k ] = dp[ k - x ] and sub( s[0:k], x ) == wordDict[i]
                    * 如果不放入: dp[ k ] = dp[ k ]
                    * 递推公式: dp[ k ] = dp[ k ] or ( dp[ k - x ] and sub( s[0:k], x ) == wordDict[i] )
                * 初始化: dp[ 0 ] = true 递推的数据基础; dp[k-x]需要初始化完;
                * 遍历顺序: 对于单词的拆分有严格的顺序要求,所以是排列数,按照先背包在物品的顺序遍历;

    """
    def wordBreak( self, s, wordDict ):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        w = len( s )
        n = len( wordDict )
        
        dp = [ False ] * ( w + 1 )
        dp[ 0 ] = True
        
        for k in range( 1, w + 1 ):
            kLenStr = s[ 0:k ]
            
            for i in range( 0, n ):
                x = len( wordDict[ i ] )
                if k >= x:
                    dp[ k ] = dp[ k ] or ( dp[ k - x ] and kLenStr[ k-x: ] == wordDict[i] )
        return dp[ w ]


if __name__ == '__main__':
    mS = "applepenapple"
    mWordDict = [ "apple", "pen" ]
    print( Solution().wordBreak( mS, mWordDict ) )
