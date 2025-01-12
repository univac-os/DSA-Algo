class Solution:
    def canBeValid(self, s: str, lock: str) -> bool:
        """
        thinking get pair of 01 but problem 11 s is () then true but will give me false
        so use stack for locked and unlocked and check them if we find pair removed locked 
        else check unlock O(n)
        """
        if len(s)%2:return False
        locked=[] #only ( 
        unlocked=[]
        for i in range(len(s)):
            if lock[i]=='0': #taking it as X we can use it ( or. )
                unlocked.append(i)
            elif s[i]=='(':
                locked.append(i)
            else: #')'
                if locked:#valid ()
                    locked.pop()
                elif unlocked:
                    unlocked.pop() #taking from unlock
                else:
                    return False
        #now we have some in locked and unlock so give them a pair
        while locked and unlocked and locked[-1]<unlocked[-1]:
            locked.pop()
            unlocked.pop()
        if locked:return False
        return True

