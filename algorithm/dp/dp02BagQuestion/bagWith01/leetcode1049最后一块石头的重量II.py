class Solution( object ):
    def lastStoneWeightII( self, stones ):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        w = sum( stones ) // 2
        n = len( stones )
        dp = [ 0 ] * ( w + 1 )
        for i in range( 0, n ):
            for k in range( w, stones[ i ] - 1, -1 ):
                dp[ k ] = max( dp[ k ], stones[ i ] + dp[ k - stones[ i ] ] )
        leftSum = sum( stones ) - dp[ w ]
        return abs( leftSum - dp[ w ] )


    def lastStoneWeightII( self, stones ):
        w = sum( stones ) // 2
        n = len( stones )
        dp = [ [ 0 ] * ( w + 1 ) for _ in range( n ) ]
        for i in range( stones[ 0 ], w + 1 ): dp[ 0 ][ i ] = stones[ 0 ]
        for i in range( 1, n ):
            for k in range( 0, w + 1 ):
                if k >= stones[ i ]:
                    dp[ i ][ k ] = max( dp[ i - 1 ][ k ], stones[ i ] + dp[ i - 1 ][ k - stones[ i ] ] )
                else:
                    dp[ i ][ k ] = dp[ i - 1 ][ k ]
        return ( sum( stones ) - dp[ n - 1 ][ w ] ) - dp[ n - 1 ][ w ]
    
    
if __name__ == '__main__':
    mStones = [ 2, 7, 4, 1, 8, 1 ]
    print( Solution().lastStoneWeightII( mStones ) )
    
        
        
        
