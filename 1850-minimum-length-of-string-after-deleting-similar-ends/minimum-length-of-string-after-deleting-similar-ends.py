class Solution:
    def minimumLength(self, s: str) -> int:
        #look like palindrome 
        l,r=0,len(s)-1
        while l<r and s[l]==s[r]:
            #greedy remove all from left and right
            tmp=s[l]
            while l<=r and s[l]==tmp:
                l+=1
            while l<=r and s[r]==tmp:
                r-=1
        return (r-l +1)
        