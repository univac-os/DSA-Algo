class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        all are same length
        sliding window but s can make repeated chars of word
        so 2 ptr to track the start index is needed 
        """
        wl=len(words[0])
        m=len(words)
        total_len=wl*m
        sl=len(s)

        if sl<total_len : return []

        tgt=Counter(words) #word:count of words
        res=[]

        #check with each index till wl
        for i in range(wl):
            left=i
            seen=defaultdict(int)
            count=0 #words in window

            j=i #this will move 
            while j+wl<=sl:
                word=s[j:j+wl]
                if word not in tgt:
                    seen.clear()
                    count=0
                    left=j+wl # start from there for next iteration
                else:
                    seen[word]+=1
                    count+=1
                    #next its occurance matches or not
                    while seen[word]>tgt[word]:
                        left_w=s[left:left+wl]
                        seen[left_w]-=1
                        count-=1
                        left+=wl#move left ptr
                    #all match then add to res
                    if count==m:
                        res.append(left)#add the left index
                        left_w=s[left:left+wl]
                        seen[left_w]-=1
                        count-=1
                        left+=wl
                j+=wl #next word index
            
        return res




        