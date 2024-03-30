class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #we want subarray with EXACT k no of unique element 
        #so count subarray with k (includes k ,k-1 ,k-2 ...)
        #find the count subarray with k-1 (include k-1 ,k-2,k-3...)
        #subtract so we get exact k 
        #O(n + n)
        #BETTER we use 3 pointer l_far, l_near ,r so this L-far is k-1 L-near -k so we get exact k 
        count=defaultdict(int)
        l_far,l_near=0,0
        res=0
        for r in range(len(nums)):
            count[nums[r]]+=1
            #2 condition to check when we have more than k 
            #one when we have eauql k
            while len(count)>k:
                #move left pointers
                count[nums[l_near]]-=1
                if count[nums[l_near]]==0:
                    count.pop(nums[l_near])#remove from hashmap
                #move l-far
                l_near+=1#go to next element
                l_far=l_near
            
            while count[nums[l_near]]>1:
                count[nums[l_near]]-=1
                l_near+=1
            
            #SECOND condition when equal to k
            if len(count)==k:
                res+=l_near-l_far+1
            #missing something what if next element has more than k items for it so we need to create 
            #l-far and l-near for it
            #we need to before adding to res
        return res

        