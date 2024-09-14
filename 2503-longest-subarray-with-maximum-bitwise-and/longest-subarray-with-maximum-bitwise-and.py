class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #better solution in single pass (NOT REQURIED)
        '''
        n < curr say 100 & 011--> 000 so we get less than curr
        n==curr we get curr
        n> curr say 111 & 011 --> 011 ,110 &011--> 010 we get ≥curr 
        '''
        size,res=0,1
        curr_max=nums[0]
        for n in nums:
            if n > curr_max:
                #we got new max
                curr_max=n
                size=1
                res=0 #reset the result as we got new max value
            elif n==curr_max:
                size+=1
            else:
                size=0
            res=max(res,size)
        return res


        #we need max value 1st
        #then check the continuous of this max number O(n+n)
        target=max(nums)
        res,curr=1,0
        for n in nums:
            if n==target:
                curr+=1
            else:
                curr=0
            res=max(res,curr)
        return res