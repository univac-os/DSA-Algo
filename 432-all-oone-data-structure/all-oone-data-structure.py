class DLL:
    def __init__(self,freq):
        self.freq=freq
        self.prev=None
        self.nxt=None
        self.keys=set() # keys with same count
class AllOne:
    """
    we want O(1) hashmap and heap gives O(logn) updation/removal
    better hashmap to store addr and linked list to find node (val) 
    if count =0 then we need remove it from ll and hashmap.
    for max and min we need to store and when inc happend check and update new max/min
    to delete ,we need to remove the node and conect prev and next so double linkedlist
    """
    def __init__(self):
        self.map={} #key-->addr of node
        self.head=DLL(float('-inf')) #dummy node at start and end
        self.tail=DLL(float('inf'))
        self.head.nxt=self.tail
        self.tail.prev=self.head
    
    def inc(self, key: str) -> None:
        if key in self.map:
            node=self.map[key] #addr of node
            freq=node.freq
            node.keys.remove(key) #remove from keys and add key to next freq val
            
            nextNode=node.nxt
            if nextNode ==self.tail or nextNode.freq!=freq+1:
                #create a new node and insertion between
                newNode=DLL(freq+1)
                newNode.keys.add(key)
                newNode.prev=node
                newNode.nxt=nextNode
                node.nxt=newNode #coneect new node to exisitng LL
                nextNode.prev=newNode
                self.map[key]=newNode
            else:
                nextNode.keys.add(key)
                self.map[key]=nextNode #update the address for key
            #if node is empty then remove the node from LL
            if not node.keys:
                self._removeNode(node)
                
        else:
            #first time addition to map
            firstNode=self.head.nxt
            if firstNode==self.tail or firstNode.freq>1:
                #create a new node
                newNode=DLL(1)
                newNode.keys.add(key)
                newNode.prev=self.head
                newNode.nxt=firstNode
                self.head.nxt=newNode
                firstNode.prev=newNode
                self.map[key]=newNode
            else:
                firstNode.keys.add(key)
                self.map[key]=firstNode
    
    def dec(self, key: str) -> None:
        if key not in self.map:
            return #key not present
        node=self.map[key]
        node.keys.remove(key)
        freq=node.freq
        if freq==1:
            del self.map[key] #remove the record from map
        else:
            #move to key to prev node postion
            prevNode=node.prev
            if prevNode==self.head or prevNode.freq!=freq-1:
                #create a new node and add this
                newNode=DLL(freq-1)
                newNode.keys.add(key)
                newNode.prev=prevNode
                newNode.nxt=node
                prevNode.nxt=newNode
                node.prev=newNode
                self.map[key]=newNode
            else:
                prevNode.keys.add(key)
                self.map[key]=prevNode
        #if node is empty then remove the node from LL
        if not node.keys:
            self._removeNode(node)
            
    def getMaxKey(self) -> str:
        if self.tail.prev==self.head:
            return "" #no key is present
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.nxt==self.tail:
            return "" #no key is present
        return next(iter(self.head.nxt.keys))
    
    def _removeNode(self,node):
        prevNode=node.prev
        nextNode=node.nxt
        prevNode.nxt=nextNode
        nextNode.prev=prevNode


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()