# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        '''
        find level sum and sort and get kth element. O(n + hlogh ) h->ht of tree,
        for balnaced tree h--> logn
        so we can use max heap and pop till k th element O(n + h + klogh) 
        here we can also use min heap of size k and pop ele if its get filled O(n + klogK)
        both max and min heap are better
        '''
        #Using MIN HEAP
        q=deque([root])
        min_heap=[] #at most size ==k
        while q:
            lev_sum=0
            for _ in range(len(q)):
                node=q.popleft()
                lev_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(min_heap,lev_sum)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
            
        return -1 if len(min_heap)<k else min_heap[0]