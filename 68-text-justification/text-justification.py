class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        greedy 
        word len add to curr line and reamaining space in between them equally 
        if after even distribution also therre are left over then give it to left to right word O(N)
        """
        res=[]
        curr,curr_len=[],0
        for w in words:
            #check if word cant fit in curr line then add space and create a new line to it 
            #include +1 space for each word mandatory len(curr) is for this take
            if curr_len+len(curr)+len(w)>maxWidth:
                # take extra spaces and distribute in between words
                extra_space=maxWidth-curr_len
                even_dist_space=extra_space//(max(1,len(curr)-1))
                remain_dist_space=extra_space%(max(1,len(curr)-1))
                for i in range(max(1,len(curr)-1)):
                    curr[i]+=" "*even_dist_space
                    if remain_dist_space:
                        curr[i]+=" "
                        remain_dist_space-=1

                res.append("".join(curr))
                curr,curr_len=[],0 #new curr line create
            
            #add word to line
            curr.append(w)
            curr_len+=len(w)
        
        #edge case last line only 1 word then add extra space to end
        last_line=" ".join(curr)
        tail_space=maxWidth-len(last_line)
        last_line+=" "*tail_space
        res.append(last_line)
        return res
