class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        dp go to jump or next position and jump
        greedy -- at each point we will see how far the person goes and check it
        """
        n=len(nums)
        jumps=0
        curr_end,far_when=0,0
        for i in range(n-1):
            far_when=max(far_when,i+nums[i])
            if i==curr_end:
                jumps+=1
                curr_end=far_when
        return jumps
        
