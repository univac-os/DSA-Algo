class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #find sub array so count the len 
        #how can we find the count --use index
        #similar take index include the value till that point 
        res=0
        max_num,max_cnt=max(nums),0
        l=0
        for r in range(len(nums)):
            if nums[r]==max_num:
                max_cnt+=1
            
            while max_cnt==k:
                #sliding window decrease the window to get count
                if nums[l]==max_num:
                    max_cnt-=1
                l+=1
            #get the lenght
            res+=l
        
        return res
        