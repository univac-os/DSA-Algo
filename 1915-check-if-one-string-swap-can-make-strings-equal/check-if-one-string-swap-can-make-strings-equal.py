class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):return False
        count=0
        if Counter(s1)!=Counter(s2):return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
        return count==2 or count==0