class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        permutation or combination works ? NO
        backtrack with count of each char better
        on each call we want to update res
        """
        res=0
        count=Counter(tiles)
        def backtrack():
            nonlocal res
            for c in count:
                if count[c]>0:
                    count[c]-=1
                    res+=1
                    backtrack()
                    count[c]+=1
            return res
        backtrack()
        return res
           
                    

    