class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        #similar to meeting room 2 -https://www.youtube.com/watch?v=FdzJmTCVyJU
        '''
        here we want how many rooms needed for meeting
        draw them in graph and check it so we want start and end point
        for any event start<end so we will sort start and end point find the start>end
        so that we need another room
        '''
        start,end=[],[]
        for s,e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        i,j=0,0
        res,room=0,0
        while i<len(intervals):#we know i will exhaust 1st
            if start[i]<=end[j]:
                i+=1
                room+=1
            else:
                #meeting is over for 1 event
                room-=1
                j+=1
            res=max(res,room)
        return res
