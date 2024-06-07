class Solution:
    def numTilings(self, n: int) -> int:
        #look dp sub problem is there based on n
        MOD=10**9+7
        domino=[False]*(n+1)
        tromino=[False]*(n+1)
        def domo(n):
            if n==0:
                return 1
            if domino[n]:
                return domino[n]
            count=0
            count+=domo(n-1) #vertical stacked
            if n-2>=0:
                count+=domo(n-2) # 2 horizontal stacked
                count+= 2*tromo(n-2) # 1 tromo stacked and 1 extra block is there
            domino[n]=count
            return count % MOD
        
        def tromo(n):
            if n==0:
                return 0
            if tromino[n]:
                return tromino[n]
            count=0
            count+=domo(n-1) #1 domo  horizontal stack
            count+=tromo(n-1) #1 tromo stacked (alternatve one)
            
            tromino[n]=count
            return count % MOD

        return domo(n)%MOD