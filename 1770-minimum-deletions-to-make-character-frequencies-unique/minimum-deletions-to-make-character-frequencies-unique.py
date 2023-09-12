class Solution:
    def minDeletions(self, s: str) -> int:
        #count the letter and and check freq is differnt
        count=Counter(s) # a-->3 ..
        res=0
        used_freq=set()
        for letter,freq in count.items():
            while freq>0 and freq in used_freq:
                freq-=1#delete it
                res+=1 
            used_freq.add(freq) #exclude 0 
        
        return res

        