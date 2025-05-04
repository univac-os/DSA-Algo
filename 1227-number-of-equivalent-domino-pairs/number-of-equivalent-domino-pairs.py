class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        [1,2] ,[2,1] ,[1,2] addition of number 
         12.     21.    12 here 21 need to made 12 so we can do min(a,b) ,max(a,b) it become uniform
         21.     12.    21
        """
        count=defaultdict(int)
        res=0
        for dx,dy in dominoes:
            a,b=min(dx,dy),max(dx,dy)
            res+=count[(a,b)]
            count[(a,b)]+=1
        return res