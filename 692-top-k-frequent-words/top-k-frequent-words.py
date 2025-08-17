class Compartor:
    def __init__(self,cnt,word):
        self.cnt=cnt
        self.word=word
    def __lt__(self,other):
        if self.cnt==other.cnt:
            return self.word>other.word #same count large lexi is smaller
        return self.cnt<other.cnt


class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        max heap of size k O(nlogk) or can we use dict and do it
        
        """
        
        min_h=[]
        count=Counter(words)

        heap=[(-cnt,w) for w,cnt in count.items()]
        heapq.heapify(heap)
        return [ heapq.heappop(heap)[1] for _ in range(k)]

        for w,cnt in count.items():
            heapq.heappush(min_h,Compartor(cnt,w))
            if len(min_h)>k:
                heapq.heappop(min_h)
        result = []
        while min_h:
            element = heapq.heappop(min_h)
            result.append(element.word)
        return result[::-1] # this correct but check count same then sort with alphablet so wrong we need custom comparator

