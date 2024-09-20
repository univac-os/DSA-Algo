class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #rabin karp -O(n)
        '''
        here instead of checking in loop each char 
        we will convert them to intergere to base of 26 (better 29 as its prime and avoid collisions)
        each time we will update the bits and check whether this bits are equal from start and reverese
        if same then remaining are needed to add in prefix 
        so O(n) and compare is O(1) as its interger comparsion
        '''
        prefix,suffix=0,0
        base=29
        last_idx=0
        mod=10**9+7
        power=0
        for i,c in enumerate(s):
            char=ord(c)-ord('a')+1 #a-1,b-2...
            prefix =(prefix*base)%mod # <<
            prefix=(prefix+char)%mod

            suffix=(suffix+char*pow(base, power, mod))%mod #>>
            power+=1

            if prefix==suffix:
                last_idx=i
        suffix=s[last_idx+1:]
        return suffix[::-1]+s

        #check reverse string and add suffix to front -> O(n2)
        def is_palindrome(l,r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l,r=l+1,r-1
            return True
        
        for r in reversed(range(len(s))):
            if is_palindrome(0,r):
                suffix=s[r+1:]
                return suffix[::-1] + s
        
        return ""
