class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        #stack to removed elements but which need to be removed ab or ba 
        #pattern start from left ab ,start from end ba- turn to ->ab 
        #greedy remove 1st ab then again search for ba so get result O(N) space->O(n)
        
        def removePair(pair,score):
            nonlocal s
            res=0
            stack=[]
            for c in s:
                if c==pair[1] and stack and stack[-1]==pair[0]:
                    stack.pop()
                    res+=score
                else:
                    stack.append(c)
            #remove we want s after removal 
            s="".join(stack)#remaining chars
            return res
        
        res=0
        pair="ab" if x>y else "ba"
        res+=removePair(pair,max(x,y)) #greedy
        res+=removePair(pair[::-1],min(x,y))
        return res