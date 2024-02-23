class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #log can used O(logn)
        #primefactor for number of power of 2 prime factor is 2 
        #get highest power 2^31 - 1 so take 2^30 % n
        return n>0 and ((1<<30) % n)==0
        #bitwise for 2 powers will have 1 000.. so check this
        return n>0 and (n & (n-1))==0
        