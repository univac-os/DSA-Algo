from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []

        counts = Counter(words)
        max_count = max(counts.values())

        # buckets[cnt] = list of words with frequency == cnt
        buckets = [[] for _ in range(max_count + 1)]
        for w, cnt in counts.items():
            buckets[cnt].append(w)

        # sort each bucket lexicographically so ties are correct
        for bucket in buckets:
            if bucket:
                bucket.sort()

        res = []
        # scan from highest frequency downwards
        for cnt in range(max_count, 0, -1):
            for w in buckets[cnt]:
                res.append(w)
                if len(res) == k:
                    return res
        return res
