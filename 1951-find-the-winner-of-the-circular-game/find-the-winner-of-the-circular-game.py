class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #simple use queue and pop and add back O(n)
        q=deque()
        for _ in range(1,n+1):
            q.append(_)

        count=0
        while len(q)>1:
            count+=1
            num=q.popleft()
            if count<k:
                q.append(num)
            else:
                #we removed so reset count
                count=0
        return q[-1]


