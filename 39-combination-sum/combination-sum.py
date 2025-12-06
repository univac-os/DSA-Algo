class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        """
        backtracking as we need all combination and we can same number 
        incldue or exlcude
        """
        def dfs(i,tgt,ds):
            if tgt==0:
                res.append(ds.copy())
                return 
            if i>=len(cand) or tgt<0:
                return
            #take it 
            if tgt>=cand[i]:
                ds.append(cand[i])
                dfs(i,tgt-cand[i],ds)
                ds.pop()
            #not take
            dfs(i+1,tgt,ds)
            
        res=[]
        cand.sort()
        dfs(0,target,[])
        return res