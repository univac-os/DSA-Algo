class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        GREEDY backtracking n! way max
        start from back side
        """
        res=[0]*(2*n-1)
        used=set()#numbers
        ans=[]
        def backtrack(i):
            if i==len(res):
                return True
            
            for num in reversed(range(1,n+1)):
                #validation
                if num in used:
                    continue 
                if num>1 and (i+num>=len(res) or res[i+num]):
                    #occupied or cant reach index
                    continue
                #add the number and check with other num
                used.add(num)
                res[i]=num
                if num>1:
                    res[i+num]=num
                #moves to next empty place
                j=i+1
                while j<len(res) and res[j]:
                    j+=1
                if backtrack(j):
                    return True
                #backtracking
                used.remove(num)
                res[i]=0
                if num>1:
                    res[i+num]=0
            

                
            

        backtrack(0)
        return res