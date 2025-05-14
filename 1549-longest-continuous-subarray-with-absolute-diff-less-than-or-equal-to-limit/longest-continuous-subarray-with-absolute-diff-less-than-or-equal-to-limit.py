class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        sliding window have min and max and check the diff and move O(N)
        but if we are removing the num which is max or min then we need to recompute the value BETTER SOLUTION heap to keep track of maxi and mini (2 heaps) and check O(nlogn)
        better stack? montonic increasing or decreasing to get max and mini val O(n)
        """
        min_q=deque()#increasing
        max_q=deque()#decreasing
        l,res=0,0
        for r in range(len(nums)):
            while min_q and nums[r]<min_q[-1]:
                min_q.pop()
            while max_q and nums[r]>max_q[-1]:
                max_q.pop()
            min_q.append(nums[r])
            max_q.append(nums[r])
            #check with limit
            while max_q[0]-min_q[0] >limit:
                if nums[l] ==max_q[0]: max_q.popleft()
                elif nums[l]==min_q[0]:min_q.popleft()
                l+=1
            res=max(res,r-l+1)
        return res