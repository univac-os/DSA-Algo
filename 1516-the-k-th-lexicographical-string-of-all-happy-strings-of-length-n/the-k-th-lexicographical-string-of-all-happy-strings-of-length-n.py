class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        get all combination 3*(2^(n-1)) and sort them in sorted and find kth 
        """
        
        def backtrack(ds,ans):
            if len(ds)==n:
                ans.append(ds.copy())
                return
            for ch in ['a','b','c']:
                if len(ds)>0 and ds[-1]==ch:
                    continue
                ds.append(ch)
                backtrack(ds,ans)
                ds.pop()
        
        ans=[]
        ds=[]
        backtrack(ds,ans)
        if len(ans)<k:
            return ""
        ans.sort()
        return "".join(ans[k-1])

