class MyCalendarTwo:
    #similar to calender 1 here we will have 2 list one is non-overlap and another for overlap
    #in overlap we will keep the common interval of 2 events O(n)
    def __init__(self):
        self.non_overlap=[] #(s,e)
        self.overlap=[]

    def book(self, start: int, end: int) -> bool:
        #1st check in overlap  if not overlap then add to non overlap list
        for s,e in self.overlap:
            if not ( e<=start or s>=end):
                return False
        for s,e in self.non_overlap:
            if not (e <=start or s>=end):
                #we need add to common interval
                self.overlap.append((max(s,start),min(e,end)))
        self.non_overlap.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)