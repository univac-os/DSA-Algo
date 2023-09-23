class Solution:
    def longestStrChain(self, words: List[str]) -> int:
      #LIS similar to this but here instead of checking increasing subseq we need check differnce in char is 1 only
      #HOW? same code as LIS but instead checking arr[i]>arr[j] check difference 
      words.sort(key=lambda x:len(x)) 
      n=len(words)
      ans=1
      dp=[1]*n

      def checkPossible(s1,s2):
        if len(s1)-len(s2)==1:
          first,second=0,0
          while first<len(s1):
            if second<len(s2) and s1[first]==s2[second]:
              first+=1
              second+=1
            #not matching that char is differnce
            else:
              first+=1
          if (first==len(s1) and second==len(s2)): return True
        return False

      for i in range(1,n):
        for j in range(i):
          if checkPossible(words[i],words[j]) and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1

        ans=max(dp[i],ans)
      
      return ans