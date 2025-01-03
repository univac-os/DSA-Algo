class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #similar to prefix sum 
        # here we will get the sum of right and minus them 
        # vowel=('a','e','i','o','u')
        vowel=set('aeiou')
        pref=[0]*(len(words)+1) # have inital start point as we will remove queries
        prev=0
        for idx,w in enumerate(words):
            if w[0] in vowel and w[-1] in vowel:
                prev+=1
            pref[idx+1]=prev
        
        res=[]
        for q in queries:
            l,r=q
            res.append(pref[r+1]-pref[l])
        return res