#Optimal solution is to sort,but each time after append and sort similar to heap
class MyCalendar:
    #brute force check with each one whether it overlapping or not O(n2)
    def __init__(self):
        self.events=[] #(s,e)

    def book(self, start: int, end: int) -> bool:
        for s,e in self.events:
            #check overlapping given event should be before start or after end
            if not (e<=start or s>=end): 
                return False
        heapq.heappush(self.events,(start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)