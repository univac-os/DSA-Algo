class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        given strictly increasing array so no duplicates
        f1 f2 (f1+f2) so we want 2 prev value only so DP can be used 
        include/exclude the number backtracking and get the length
        OR fix 2 element and find fib series O(n2*O(1))
        """
        arr_set=set(arr)
        res=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev,curr=arr[i],arr[j]
                nxt=prev+curr
                length=2
                while nxt in arr_set:
                    length+=1
                    prev=curr
                    curr=nxt
                    nxt=prev+curr
                    res=max(res,length)
        return res