class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #sort by start time
        # we need to check room used by meeting and available room
        #give room to less number so sort or heap 
        #used as sorted so heap (min heap)
        meetings.sort()
        available=[_ for _ in range(n)] #room for meeting 
        used=[] #(end_time,room)
        count=[0]*n #how many time a room is used

        for start,end in meetings:
            #room is available and not used
            while used and start>=used[0][0]:
                #room available for meeting
                _,room =heapq.heappop(used)
                heapq.heappush(available,room) #used that room
            #tow case room is available or not.if not wait
            if not available:
                #all room are full
                #take the least end room from used
                end_time,room=heapq.heappop(used)
                #wait till room empty and meeting time add SO UPDATE THE END TIME
                end=end_time + (end-start)
                heapq.heappush(available,room) #used that room
            
            #update the used so get the room and add to used
            room=heapq.heappop(available) #get the room
            heapq.heappush(used,(end,room))
            
            count[room]+=1 

        return count.index(max(count)) #get the index(room) maximum used

        