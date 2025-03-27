class Solution( object ):
    def uniquePathsWithObstacles( self, obstacleGrid ):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # -- 相较于 leetcode62,本题只是在路上增加了障碍物 --
        # -- 还是沿leetcode62的处理方式 dp[i][k] = dp[i-1][k] + dp[i][k-1],不过如果是障碍物dp[i][k]设置为0,可以理解为,该格点有障碍物无法到达 --

        m, n = len( obstacleGrid ), len( obstacleGrid[ 0 ] )

        dp = [ [ 0 ] * n for _ in range( m ) ]
        for i in range( n ):
            if obstacleGrid[ 0 ][ i ] == 1: break
            dp[ 0 ][ i ] = 1
        for i in range( m ):
            if obstacleGrid[ i ][ 0 ] == 1: break
            dp[ i ][ 0 ] = 1
        for i in range( 1, m ):
            for k in range( 1, n ):
                if obstacleGrid[ i ][ k ] == 0:
                    dp[ i ][ k ] = dp[ i - 1 ][ k ] + dp[ i ][ k - 1 ]
        return dp[ m - 1 ][ n - 1 ]

    def uniquePathsWithObstacles( self, obstacleGrid ):
        m, n = len( obstacleGrid ), len( obstacleGrid[ 0 ] )
        dp = [ 0 ] * n
        for i in range( n ):
            if obstacleGrid[ 0 ][ i ] == 1: break
            dp[ i ] = 1
        for i in range( 1, m ):
            # -- 每行开始,初始化dp[0] --
            if obstacleGrid[ i ][ 0 ] == 1: dp[ 0 ] = 0
            for k in range( 1, n ):
                if obstacleGrid[ i ][ k ] == 1: dp[ k ] = 0
                else: dp[ k ] += dp[ k - 1 ]
        return dp[ n - 1 ]
                
                
if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print( Solution().uniquePathsWithObstacles( obstacleGrid ) )
