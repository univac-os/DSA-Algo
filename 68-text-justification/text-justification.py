class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        curr_line,length=[],0
        i=0
        while i<len(words):
            #lines completes with words add spaces 
            #present word lenght + 1 space b/w them + new word
            if length+len(curr_line)+len(words[i])>maxWidth:
                #we cant add this word to line so add spaces b/w the already words
                #and also greedy way as mentioned
                extra_space=maxWidth-length
                spaces=extra_space//max(1,len(curr_line)-1) #word present in line
                reminder=extra_space%max(1,len(curr_line)-1) #greedy 
                for j in range(max(1,len(curr_line)-1)):
                    curr_line[j]+=" "*spaces
                    if reminder:
                        curr_line[j]+=" "
                        reminder-=1

                res.append("".join(curr_line)) # add to res
                curr_line,length=[],0 # new line

            #add word to  the line 
            curr_line.append(words[i])
            length+=len(words[i])
            i+=1

        #edge case when we are take last line and no words then add spaces after words
        last_line=" ".join(curr_line)
        tail_spaces=maxWidth-len(last_line)
        last_line+= " "*tail_spaces
        res.append(last_line)
        return res