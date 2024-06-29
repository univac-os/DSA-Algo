class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #graph bfs as we want mini count to reach end adn check 1..6
        #how to get where we are on board? (r,c) r/n annd c%n
        #we need to reverse board as we start from bottom 
        def nextPostion(square):
            #we get row and col position
            r=(square-1)//n #starting from 0
            c=(square-1)%n
            #check based on row we are moving from l to r and r to l
            if r%2:#odd r to l
                c=n-1-c
            
            return [r,c]
        board.reverse()
        n=len(board)
        q=deque() #[(square,count)]
        q.append([1,0]) #start
        visit=set()
        while q:
            square,moves=q.popleft()
            for i in range(1,7):
                nextSq=square+i
                r,c=nextPostion(nextSq)#get next position 
                if board[r][c]!=-1:
                    nextSq=board[r][c]
                if nextSq==n*n:
                    return moves+1
                #before this check we are at end
                if nextSq not in visit:
                    visit.add(nextSq)
                    q.append([nextSq,moves+1])
        return -1
