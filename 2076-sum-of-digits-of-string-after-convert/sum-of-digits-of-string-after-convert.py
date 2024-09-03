class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #O(N)
        curr=0
        for c in s:
            pos=str(ord(c)-ord('a')+1)
            if int(pos)>9:
                curr=curr+int(pos[0])+int(pos[-1])
            else:
                curr+=int(pos)
        for i in range(1,k):
            digit=0
            while curr>0:
                digit+=curr%10
                curr//=10
            curr=digit
    
        return curr
