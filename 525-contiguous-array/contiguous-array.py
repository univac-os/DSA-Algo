class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #O(n2) make sub array and check 1 and 0 counts
        #To reduce time complexity Sliding window ,have check of 1 and 0
        #but from where we need to remove the value start or end
        #use hashmap to keep index and diff of 1 and 0 as key
        #DOUBT-will the diff of 1-0 can be same value in between also
        #SO here we need to check where we need to remove idx from start or end
        #so check this 1-0 in hashmap and remove that element
        zero,one=0,0
        res=0
        diff={} #count[1]-count[0] -->index
        for idx,n in enumerate(nums):
            if n==0:
                zero+=1
            else:
                one+=1
            if one-zero not in diff:
                diff[one-zero]=idx 
            
            if one==zero:
                res=one+zero
            else:
                #remove idx 
                res=max(res,idx-diff[one-zero])
        
        return res
            
        