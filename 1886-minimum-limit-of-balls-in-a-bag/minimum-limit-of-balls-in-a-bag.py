class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        '''
        Greedy take max value and divide equal part and go it
        but say 9 --> 4,5-->4,2,3 we get 4 but answer is 3 so
        check for each number 1..9 where i want to divide and get it ball 
        use binary search O(nlog(max_value))
        '''
        def is_valid(req_ball):
            #say 9/4-> 2.25 ->ceil is 3--> 3-1=2 so in 2 operation we can get
            ops=0
            for n in nums:
                ops+=ceil(n/req_ball)-1
                if ops>maxOperations:
                    return False
            return True

        l,r=1,max(nums)
        while l<=r:
            m=(l+r)//2
            if is_valid(m):
                #greddy find less max
                r=m-1
            else:
                l=m+1
        return l
