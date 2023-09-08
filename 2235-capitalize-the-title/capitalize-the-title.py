class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=title.split()
        res=[]
        for word in words:
            res.append(word.title() if len(word)>2 else word.lower())
        return " ".join(res)