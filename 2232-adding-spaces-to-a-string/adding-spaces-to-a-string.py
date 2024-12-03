class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        res.append(s[0:spaces[0]])
        for j in range(1,len(spaces)):
            res.append(s[spaces[j-1]:spaces[j]])
        res.append(s[spaces[-1]:])
        return " ".join(res)