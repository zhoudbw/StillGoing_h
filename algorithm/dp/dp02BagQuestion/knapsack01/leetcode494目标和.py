class Solution( object ):
    """
        给定一个非负整数数组 nums, 和一个目标数 target.
        现在你有两个符号 +和-, 对于数组中的任意一个整数, 你都可以从 +或- 中选择一个符号添加在前面.
        返回可以使最终数组和为目标数 target 的所有添加符号的方法数.
        
        -- 问题转化 --
        对于target的获取, 满足( 左边的组合(+连接) - 右边的组合(+连接) = target )
        若有左边的组合为left, 那么右边的组合为 sum( nums ) - left,
        则: left - ( sum( nums ) - left ) = target => left = 0.5 * ( target + sum( nums ) )
        则: 问题转化求数字组合之和为 0.5 * ( target + sum( nums ) ) 的种类数,
        通过这样的转化,就不需要考虑+和-的使用,只需要关注nums的组合即可.
        
        -- 解决方法 --
        -- 方法1: 利用回溯, 找到所有的组合情况, 当该组合的集合之和 == left时, 找到一种, 最终就能确定种类数 --
        -- 方法2: 动态规划 --
            -- 任取[0, i]件物品, 装满w = left的背包 => 典型背包问题 --
            -- 分析 --
            -- 1. 确定dp和下标的含义: dp[i][k] 从[0,i]的物品中任取, 能够装满容量为k的背包的所有种类数 --
            -- 2. dp[i][k]的来源, 放入i物品的种类数 + 不放入物品i的种类数,即 dp[i][k] = dp[i-1][k] + dp[i-1][k-i物品的重量] --
            -- 3. 根据递推公式很容易初始化dp数组,i-1层需要初始化,需要注意k-i物品重量不要小于0 --
            -- 4. 遍历顺序依旧沿用前面的习惯, 先遍历物品,再遍历重量,从左到右 --
    """

    def findTargetSumWays( self, nums, target ):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # -- 存在影响dp数组初始化的情况,优先处理 --
        totalSum = sum( nums )
        if (totalSum + target) % 2 == 1: return 0
        if abs( target ) > totalSum: return 0   # -- 如果target 的绝对值已经大于sum, 那么也是没有方案的 ( 避免出现w为负值的情况 ) --

        # -- 动态规划 --

        w = ( totalSum + target ) // 2  # -- *** ---
        n = len( nums )

        dp = [ [ 0 ] * ( w + 1 ) for _ in range( n ) ]

        # -- 初始化dp数组 ( 比较难点的地方 ) --
        # --    这里的初始化需要特别注意,需要物品数值就是0的情况 --
        if 0 < nums[ 0 ] < w + 1: dp[ 0 ][ nums[ 0 ] ] = 1
        
        zeroCount = 0
        for i in range( 0, n ):
            if nums[ i ] == 0: zeroCount += 1
            # -- 算数组里有x个0, 然后按照组合数量求种类数, 即 2^t  --
            dp[ i ][ 0 ] = 2 ** zeroCount
            
        for i in range( 1, n ):
            for k in range( 1, w + 1 ):
                if k - nums[ i ] >= 0:
                    dp[ i ][ k ] = dp[ i - 1 ][ k ] + dp[ i - 1 ][ k - nums[ i ] ]
                else:
                    dp[ i ][ k ] = dp[ i - 1 ][ k ]

        return dp[ n - 1 ][ w ]

    """
        压缩dp数组的做法
    """
    def findTargetSumWays( self, nums, target ):
        totalSum = sum( nums )
        if (totalSum + target) % 2 == 1: return 0
        if abs( target ) > totalSum: return 0

        w   = ( totalSum + target ) // 2
        n   = len( nums )
        dp  = [ 0 ] * ( w + 1 )
        
        if 0 < nums[ 0 ] < ( w + 1 ): dp[ nums[ 0 ] ] = 1
        dp[ 0 ] = nums[ 0 ] == 0 and 2 or 1
        
        for i in range( 1, n ):
            for k in range( w, nums[ i ] - 1, -1 ):
                dp[ k ] = dp[ k - nums[ i ] ] + dp[ k ]
        return dp[ w ]
    
    """
        其实上述代码的初始化完全不需要这么复杂,
        第0层的时候也可以放入循环中递推出来,  对于递推公式: dp[ k ] = dp[ k - nums[ i ] ] + dp[ k ]
        即 dp[ k ] += dp[ k - nums[ i ] ] 表示能够放下nums[i]时, 装满容量为k的背包的种类数 = 装入nums[i]的种类数 + 不装入nums[i]的种类数
        所以,初始化dp[0] = 1表示,不放入任何物品时,容量为0的背包装满的最大种类数, 
        递推中,如果dp[0]能够放下nums[i],种类数就更新为: 装入nums[i]的种类数+不转入nums[i]的种类数, 即 dp[0] = dp[ 0 - nums[i]]+dp[0]
    """
    def findTargetSumWays( self, nums, target ):
        totalSum = sum( nums )
        if ( totalSum + target ) % 2 == 1: return 0
        if abs( target ) > totalSum: return 0
    
        w   = ( totalSum + target ) // 2
        n   = len( nums )
        dp  = [ 0 ] * ( w + 1 )
        dp[ 0 ] = 1
        for i in range( 0, n ):
            for k in range( w, nums[ i ] - 1, -1 ):
                dp[ k ] += dp[ k - nums[ i ] ]
        return dp[ w ]
        
                
if __name__ == '__main__':
    mNums = [ 0, 0, 0, 0, 0, 0, 0, 0, 1 ]
    mTarget = 1
    print( Solution().findTargetSumWays( mNums, mTarget ) )
