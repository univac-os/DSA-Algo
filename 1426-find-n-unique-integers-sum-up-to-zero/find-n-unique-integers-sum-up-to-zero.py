class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
        we can any numbers half + and remaining - so have a replica number
        """
        res=[]
        for i in range(1,n//2+1):
            res.append(i)
            res.append(-i)
        if n%2:
            res.append(0)
        return res
        