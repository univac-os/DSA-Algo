class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        #start from end and break large value into small piece keeping greedy
        #we want minimum so break all close to each other 
        ans=0
        n=len(nums)
        last=nums[-1]

        for i in range(n-2,-1,-1):
            if nums[i]>last:
                #break the num into peices
                num_break=nums[i]//last #ex 7//3 -2 reminder 1 so we need to break into 3 parts
                if nums[i]%last:# reminder is there
                    num_break+=1
                last=nums[i]//num_break  # greedy [1,3,3] or [2,2,3] 2 is better 
                ans+=num_break -1

            else:#no break needed
                last=nums[i]
            
        return ans