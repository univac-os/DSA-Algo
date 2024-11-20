class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        backtracking moving left and moving right get the minimum length

        better find the subarray where we can get extra element so from requires+x=full
        x=full-requires
        so how sliding window to get the count of a,b,c
        """
        # aab aaaa caabc
        count=[0,0,0]#a,b,c
        for c in s:
            count[ord(c)-ord('a')]+=1
        if min(count)<k:
            return -1
        l=0
        res=float('-inf')
        for r in range(len(s)):
            #get the char and check in count array 
            count[ord(s[r])-ord('a')]-= 1
            while min(count)<k:
                count[ord(s[l])-ord('a')]+=1
                print(min(count))
                l+=1
            res=max(res,r-l+1)
        return len(s)-res

            