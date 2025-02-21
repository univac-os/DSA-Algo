class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        get all combination 3*(2^(n-1)) and sort them in sorted and find kth 
        """
        ans=[]
        def backtrack(ds,ans):
            if len(ds)==n:
                ans.append(ds)
                return
            for ch in ['a','b','c']:
                if len(ds)>0 and ds[-1]==ch:
                    continue
                backtrack(ds+ch,ans)
        
        backtrack("",ans)
        if len(ans)<k:
            return ""
        ans.sort()
        return ans[k-1]

