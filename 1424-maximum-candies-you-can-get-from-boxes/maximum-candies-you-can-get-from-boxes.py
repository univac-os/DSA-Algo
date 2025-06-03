class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
        looks simulation 
        graph type connect node to 0 -->containedboxes
        union find not req so simple bfs can be done
        but if i take a val and check no key then later i can use same val and get opened later
        so we need opened set to have which are opened and locked to again use it
        """
        q=deque(initialBoxes)
        res=0
        opened,locked=set(),set()
        while q:
            box =q.popleft()
            if box in opened:
                continue #skip it
            if status[box]==1:
                res+=candies[box]
                opened.add(box)
                for k in keys[box]:
                    status[k]=1 #update the status to unlock it
                    if k in locked:
                        q.append(k)
                        locked.remove(k)

                for b in containedBoxes[box]:
                    q.append(b)
            else:
                #locked for now
                locked.add(box)
        return res


