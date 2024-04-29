class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        #for everyone lock go +1 and -1 O(10000)
        def nextLock(lock):
            res=[]
            for i in range(4):
                #+1
                digit=str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                #-1
                digit=str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res
        q=deque()
        visited=set(deadends)#add in deadends in visited as we wont pass after deadends
        q.append(["0000",0]) #lock,turn
        while q:
            lock,turn=q.popleft()
            if lock==target:
                return turn
            nextTurn=nextLock(lock)
            for t in nextTurn:
                if t not in visited:
                    q.append([t,turn+1])
                    visited.add(t)
        return -1