class Solution( object ):
    def numTrees( self, n ):
        """
        :type n: int
        :rtype: int
        """
        
        # if n == 0: return 1     # -- 空树,也是二叉搜索树 --
        
        # -- dp[i]表示i个节点能够组成的二叉搜索树的个数 --
        # -- 确定递推公式: dp[i]的来源有,以1为根节点二叉搜索数个数+以2为根节点的二叉搜索树个数+...+以i为根节点的二叉搜索树的个数,
        #    举例来说: 以n==3而言, 以1为根节点,根据二叉搜索树的特性,1的左右两侧都是二叉搜索树,所以以1为根节点的二叉搜索树个数为dp[0]*dp[2],
        #    具体来说,由于n==3,当1为根节点时,比1小的数个数为0,比1大的数个数为2,所以以1为根节点的二叉搜索树个数为,0个节点的二叉搜索树个数和2个节点的二叉搜索树个数的组合,
        #   `即，dp[0]*dp[2],以2为根节点的二叉搜索树个数为dp[1]*dp[1],以3为根节点的二叉搜索树个数为dp[2]*dp[0],
        #    所以: dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0] ==> 递推公式 --
        # -- 初始化显而易见: dp[0] dp[1] dp[2] 足以,更进一步,初始化dp[0]就可以了 --
        # -- 遍历顺序,显然以1...i为根节点的二叉搜索树之和,且后者由前者推出 --
        dp = [ 0 ] * ( n + 1 )
        dp[ 0 ] = 1
        for i in range( 1, n + 1 ):
            for k in range( 1, i + 1 ):
                dp[ i ] = dp[ i ] + dp[ k - 1 ] * dp[ i - k ]
        return dp[ n ]
    
    
if __name__ == '__main__':
    print( Solution().numTrees( 3 ) )
       