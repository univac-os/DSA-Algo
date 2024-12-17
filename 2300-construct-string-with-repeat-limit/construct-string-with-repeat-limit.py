class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        #count and sort 
        #but after repeatlimit we will take out the char and take next one char and add back
        #max heap O(n log26)
        count=Counter(s)
        max_H=[(-ord(c),cnt)for c,cnt in count.items()]
        heapq.heapify(max_H)#O(n)
        res=[]
        while max_H:
            curr_char,cnt=heapq.heappop(max_H)
            char=chr(-curr_char)
            curr_cnt=min(cnt,repeatLimit)
            res.append(char*curr_cnt)
            #check still there are more char left 
            if cnt-curr_cnt>0 and max_H:
                #take next char one time and add prev char
                nxt_char,nxt_cnt=heapq.heappop(max_H)
                res.append(chr(-nxt_char))
                if nxt_cnt>1:
                    heapq.heappush(max_H,(nxt_char,nxt_cnt-1))
                heapq.heappush(max_H,(curr_char,cnt-curr_cnt))
        return ''.join(res)
