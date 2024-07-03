class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #finally we need min and max value from array so greedy
        #eliminate all large value /all smaller value so sliding window
        #sort to get the value of small and large on both side -O(logn)
        #ex-- 1 3 4 7 9 10 13 len-7
        #.     0   3 so 1 - 7 (remove 9 10 13)
        #      1   2 so 3 -9
        #      2    1.so 4 - 10 
        #      3    0. so 7 -13
        if len(nums)<=4:
            return 0
        nums.sort()
        res=float('inf')
        for l in range(4):
            r=len(nums)-4 +l
            res=min(res,nums[r]-nums[l])
        return res