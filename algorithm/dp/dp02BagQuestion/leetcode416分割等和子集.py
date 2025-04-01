class Solution( object ):

    # -- 方法1: 暴力回溯求解出所有分割情况,只要分割集合满足sum( 子集 ) = sum( 全集 ) / 2, return true --
    def canPartition( self, nums ):
        """
        :type nums: List[int]
        :rtype: bool
        """
        subSetResultList = []

        def backtracking( iNums, iStartIndex, iPath, iResult ):
            completeSetSum = sum( iNums )
            subsetSum = sum( iPath )
            if subsetSum > completeSetSum / 2.0:
                return
            if subsetSum == completeSetSum / 2.0:
                iResult.append( iPath[ :: ] )
                return
            for i in range( iStartIndex, len( iNums ) ):
                iPath.append( iNums[ i ] )
                backtracking( iNums, i + 1, iPath, iResult )
                iPath.pop()

        backtracking( nums, 0, [], subSetResultList )
        return len( subSetResultList ) > 0
# -- 超出时间限制  37 / 144 个通过的测试用例 --

    # -- 方法2: 动态规划 01背包 --
    def canPartition( self, nums ):
        """
            只要找到集合里能够出现 sum / 2 的子集总和，就算是可以分割成两个相同元素和子集
            本题的本质是，能否把容量为 sum / 2的背包装满
            这是 背包算法可以解决的经典类型题目
            -- 很关键的: 如何将其对应到01背包模型上 --
                集合中的数字,分割子集,显然集合中的数字每次只可以使用一次 —— 满足01背包选取原则
                在01背包中，物品有属性重量和价值(两个维度)，将本题中数字(一个数字只有一个维度，即 重量等于价值)
                    也抽象成两个维度(重量和价值, 重量=数字的数值,价值=数字的价值)
                    那么，背包的容量就是背包能装下的最大价值，即背包的最大价值为sum / 2   —— 至此就可以使用01背包的代码去解决问题
            ----
            注意初始化:如果题目给的价值都是正整数那么非0下标都初始化为0就可以了，如果题目给的价值有负数，那么非0下标就要初始化为负无穷
            这样才能让dp数组在递推的过程中取得最大的价值，而不是被初始值覆盖了。
        """
        # 1 <= nums.length <= 200
        # 1 <= nums[i] <= 100
        if sum( nums ) % 2 == 1: return False
        
        w = sum( nums ) // 2
        dp = [ 0 ] * ( w + 1 )
        for i in range( 0, len( nums ) ):
            for k in range( w, nums[ i ] - 1, -1 ):
                dp[ k ] = max( dp[ k ], nums[ i ] + dp[ k - nums[i ] ] )
        return dp[ w ] == sum( nums ) / 2
# -- 01背包相对于本题，主要要理解，题目中物品是nums[i]，重量是nums[i]，价值也是nums[i]，背包体积是sum/2。 --

    def canPartition( self, nums ):
        if sum( nums ) % 2 == 1: return False
        
        w, n = sum( nums ) // 2, len( nums )
        dp = [ [ 0 ] * ( w + 1 ) for _ in range( n ) ]
        for i in range( nums[ 0 ], w + 1 ): dp[ 0 ][ i ] = nums[ 0 ]
        for i in range( 1, n ):
            for k in range( 0, w + 1 ):
                if k >= nums[ i ]: dp[ i ][ k ] = max( dp[ i - 1 ][ k ], nums[ i ] + dp[ i - 1 ][ k - nums[ i ] ] )
                else: dp[ i ][ k ] = dp[ i - 1 ][ k ]
        return dp[ n - 1 ][ w ] == w

if __name__ == '__main__':
    mNums = nums = [1,5,11,5]
    print( Solution().canPartition( mNums ) )
