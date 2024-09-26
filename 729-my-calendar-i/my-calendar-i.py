#Optimal solution is to sort,but each time after append and sort similar to heap O(nlogn)
#worst it can go to O(n2)
#BETTER --- similar to heapq ,here we can use BST based on start and end we add node to left or right O(n)
class BST:
    def __init__(self,start,end):
        self.left,self.right=None,None
        self.start,self.end=start,end
    
    def insert(self,start,end):
        curr=self
        while True:
            if start >=curr.end:
                #add to right ,check right side
                if curr.right==None:
                    curr.right=BST(start,end)
                    return True
                curr=curr.right
            elif end <=curr.start:
                #add to left ,check left side
                if curr.left==None:
                    curr.left=BST(start,end)
                    return True
                curr=curr.left
            else:
                #overlapp
                return False


class MyCalendar:
    def __init__(self):
        self.root=None

    def book(self,start,end):
        if not self.root:
            self.root=BST(start,end)
            return True
        return self.root.insert(start,end)

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