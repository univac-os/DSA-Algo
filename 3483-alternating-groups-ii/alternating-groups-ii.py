class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        extend the array with k and do the sliding window O(n+k) --> O(n)
        we want total count of shrink the window

        """
        for i in range(k-1):
            colors.append(colors[i])
        res=0
        l,r=0,1

        while r<len(colors):
            #same color move to next
            if colors[r]==colors[r-1]:
                l=r
                r+=1
                continue
            r+=1
            if r-l<k:
                continue
            res+=1
            l+=1 #shrink window
        return res
