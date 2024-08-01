class Solution:
    def minimumDeletions(self, s: str) -> int:
        #count a and b we need a point where no a no right side and b on left side
        #start first get all a count and then while movig reduce a count if a is take on left side
        #increase b count if b is coming 
        #sum of these are the deletion of char
        a_in_right=s.count('a')
        b_in_left=0
        res=len(s)
        for i,c in enumerate(s):
            #all a on left side
            if c=='a':
                a_in_right-=1
            res =min(res,a_in_right+b_in_left)
            #we got b so next time we need to delete it
            if c=='b':
                b_in_left+=1
        return res