class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        so we need count of char and take the more no of char first and check with prev 
        so we need keep the prev on hold till next operation
        """
        count=Counter(s)
        max_h=[[-cnt,c] for c,cnt in count.items()]
        heapq.heapify(max_h)
        prev=None
        res=""
        while max_h or prev:
            if prev and not max_h:return "" #there is prev value and no value to keep next to it
            cnt,char=heapq.heappop(max_h)
            cnt+=1 #decrease count
            res+=char
            #keep hold the this char to next iteraton but before this check with prev present or we can take in next loop
            if prev:
                heapq.heappush(max_h,prev)
                prev=None
            if cnt!=0:# so this char is prev now
                prev=[cnt,char]
        return res