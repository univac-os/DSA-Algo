class Solution:
    def longestPalindrome(self, s: str) -> int:
        #Hashmap if even num of char then increase +2
        #if odd num is there increase +1 
        #better use hashSet  even char remove from set +2 
        #odd char then add to set +1
        seen=set()
        res=0
        for c in s:
            if c in seen:
                #even no of char
                seen.remove(c)
                res+=2
            else:
                #odd no of char
                seen.add(c)
        #if there are any odd no of char (here 1 char) then +1
        return res+1 if seen else res
        