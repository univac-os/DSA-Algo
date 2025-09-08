class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        number should have 0 in it
        """
        for a in range(1,n):
            b=n-a
            if "0" not in str(a)+str(b):
                return [a,b]
            

