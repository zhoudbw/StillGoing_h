# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution( object ):
    
    # -- 如果不是二叉搜索树，最直观的方法一定是把这个树都遍历了，用map统计频率，把频率排个序，最后取前面高频的元素的集合。 --
    # -- 但 既然是搜索树，它中序遍历就是有序的。 --
    def findMode( self, root ):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.modeList = []
        self.preNode  = None  # -- 存储前一个节点 --
        self.maxCount = 0  # -- 当前树中最大出现频率 --
        self.memCount = 0  # -- 当前节点的频率 --
        
        def dfsInorder( iCurNode ):
            if not iCurNode: return
            
            dfsInorder( iCurNode.left )
            
            # -- 统计频率 --
            if not self.preNode:
                # -- 比较第一个元素 --
                self.memCount = 1
            elif self.preNode.val == iCurNode.val:
                # -- 当前值和前一个值相同 --
                self.memCount += 1
            else:
                # -- 当前值和前一个值不同 --
                self.memCount = 1
            
            # -- 更新最大频率和结果 --
            if self.memCount > self.maxCount:
                self.maxCount = self.memCount
                # -- 清空并加入当前值 --
                self.modeList = [ iCurNode.val ]
            elif self.memCount == self.maxCount:
                self.modeList.append( iCurNode.val )
            
            # -- 更新前一个节点 --
            self.preNode = iCurNode
            
            dfsInorder( iCurNode.right )
        
        dfsInorder( root )
        return self.modeList