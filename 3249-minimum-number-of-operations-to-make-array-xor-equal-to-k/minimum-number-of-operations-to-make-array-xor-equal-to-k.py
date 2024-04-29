class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #check with example
        #if odd 1 then we get 1
        #we need to check on many 1 in final output
        final_xor=0
        for n in nums:
            final_xor^=n

        return bin(final_xor^k).count('1')
        count=0
        while k or final_xor:
            if(k%2) !=final_xor^2:
                count+=1
            k //=2
            final_xor //=2
        return count
        