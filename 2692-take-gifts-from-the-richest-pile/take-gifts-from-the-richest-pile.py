class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # take max value and sqrt and again add so we are dynamically changing so maxHEap
        #O(n+ klogn)
        gifts=[-_ for _ in gifts]
        heapq.heapify(gifts)#maxHeap
        for _ in range(k):
            n=-heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(sqrt(n)))
        return -sum(gifts)
