class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)#hashmap char-->count
        mh=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(mh)#most freq char

        prev=None
        res=""
        while mh or prev:
            if prev and not mh: # aaab --> aba prev=a mh is empty
                return ""
            
            cnt,char=heapq.heappop(mh)
            cnt+=1 #decrease by 1
            res+=char

            if prev:#prev is present add to heap for next loop
                heapq.heappush(mh,prev)
                prev=None

            if cnt!=0:#char occurance present
                prev=[cnt,char] # this should be done at last

        return res