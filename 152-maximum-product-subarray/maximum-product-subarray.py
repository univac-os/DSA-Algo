class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n2) --nested loop
        #observation if -ve numb is there either prefix or suffix is max
        #if 0 then prefix or suffix 
        #if even -ve numb then individual -ve num same thing prefix or suffix
        prefix,suffix=1,1
        res=float('-inf')
        n=len(nums)
        for i in range(n):
            if prefix==0:
                #reset
                prefix=1
            if suffix ==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-1-i]
            res=max(res,prefix,suffix)
        return res