class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #if we want also pair then simple use min heap 1-->(0,3,4) and use for loop and get pair (0,3) (0,4) (3,4)
        
        
        # 1. nCr formula nc2=n*n-1 //2
        count=Counter(nums) #1 -->3
        res=0
        for c in count.values():
            res+= (c*(c-1))//2
        
        return res
        #2. have count of pair and when we get new it can form new pair with prev count
        count={} #n -->C
        res=0
        for n in nums:
            if n in count:
                res+=count[n] #add prev count
                count[n]+=1 #update
            else:
                count[n]=1
        return res

        
        # 1. nCr formula nc2=n*n-1 //2
        count=Counter(nums) #1 -->3
        res=0
        for n,c in count.items():
            res+= (c*(c-1))//2
        
        return res