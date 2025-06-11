class Solution:
    def maxEnvelopes(self, envl: List[List[int]]) -> int:
        """
        sort and 2 pointer but problem is we need to check for each case so dp
        start from back but we need to check till end O(n2) gives time limit exceed so 
        better nlogn how sorting based on width first so width is okay then based on height find better if same width then have the ht in descending order so that LIS and get the boxes
        """
        envl.sort(key=lambda x:(x[0],-x[1]))
        ht=[h for _,h in envl]
        #we will make LIS based on  ht as based on width we are sorted
        lis=[]
        for h in ht:
            idx=bisect_left(lis,h)
            if idx==len(lis):
                lis.append(h)
            else:
                lis[idx]=h
        return len(lis)

        envl.sort()
        n=len(envl)
        dp=[1]*(n+1)
        for i in range(n-2,-1,-1):
            j=i+1
            while j<n:
                if envl[i][0]<envl[j][0] and envl[i][1] <envl[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
                j+=1
        return max(dp)

            