# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from algorithm.tree.TreeNode import TreeNode


class Solution( object ):
    
    def getMaxValue( self, nums ):
        # -- 0 <= nums[i] <= 1000 --
        # -- 1 <= nums.length <= 1000 --
        # -- nums 中的所有整数 互不相同 --
        
        maxValue, maxValueIdx = nums[ 0 ], 0
        for i in range( 1, len( nums ) ):
            if nums[ i ] > maxValue:
                maxValue, maxValueIdx = nums[ i ], i
        return maxValue, maxValueIdx
    
    # -- 额外开辟数组 --
    def constructMaximumBinaryTree( self, nums ):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums: return None
        
        maxValue, maxValueIdx = self.getMaxValue( nums )
        numsLeft = nums[ :maxValueIdx ]
        numsRight = nums[ maxValueIdx + 1: ]
        
        left = self.constructMaximumBinaryTree( numsLeft )
        right = self.constructMaximumBinaryTree( numsRight )
        return TreeNode( maxValue, left, right )
    
    # -- 注意类似用数组构造二叉树的题目，每次分隔尽量不要定义新的数组，而是通过下标索引直接在原数组上操作，这样可以节约时间和空间上的开销 --
    def constructMaximumBinaryTree( self, nums ):
        
        # -- 注: 数组 [ iBeginIndex, iEndIndex ) 左闭右开 --
        def dfsMaxTreeByIdx( iNums, iBeginIndex, iEndIndex ):
            if iBeginIndex >= iEndIndex: return None
            
            iMaxValIndex, iMaxVal = iBeginIndex, iNums[ iBeginIndex ]
            for i in range( iBeginIndex, iEndIndex ):
                if iNums[ i ] > iMaxVal: iMaxValIndex, iMaxVal = i, iNums[ i ]
            
            iRoot = TreeNode( iMaxVal )
            iRoot.left = dfsMaxTreeByIdx( iNums, iBeginIndex, iMaxValIndex )
            iRoot.right = dfsMaxTreeByIdx( iNums, iMaxValIndex + 1, iEndIndex )
            return iRoot
        
        return dfsMaxTreeByIdx( nums, 0, len( nums ) )