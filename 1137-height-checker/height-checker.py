class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #sort and count the differ value O(nlogn +n)
        #use counting sort O(n+max_valof n)
        maxi=max(heights)
        count=[0]*(maxi+1)
        for n in heights:
            count[n]+=1
        expected=[]
        for i in range(0,maxi+1):
            if count[i]>0:
                expected.extend([i]*count[i])
        res=0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                res+=1
        return res
