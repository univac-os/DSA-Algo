class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #looks at 560 leetocde
        #we need sub array where sum %k=0 so think 2 ptr
        #l,r move it till end and check % ,then move l towards r and check %
        #so looking at this we can see we are removing some part from total sum
        #meaning removing prefix sum till l ptr from total
        #we will reminder value stored to get how many times we got get k in between them
        prefix_cnt={0:1}
        res=0
        prefix_sum=0
        for n in nums:
            prefix_sum+=n
            rem=prefix_sum%k
            if rem in prefix_cnt:
                res+=prefix_cnt[rem]
            prefix_cnt[rem]=1+prefix_cnt.get(rem,0)
        return res