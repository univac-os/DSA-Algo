class NumberContainers:
    """
    we can use array to store index --> value but we dont have size of array
    so will use  2 hashmap  1--> idx -> val and 2--> val->idx
    """
    def __init__(self):
        self.nToI=defaultdict(SortedSet)
        self.iToN={}

    def change(self, index: int, number: int) -> None:
        if index in self.iToN:
            #we have index of change the value
            prev_val=self.iToN[index]
            self.nToI[prev_val].remove(index)
            if not self.nToI[prev_val]:  # Clean up empty sets
                del self.nToI[prev_val]

        self.iToN[index]=number
        self.nToI[number].add(index)


    def find(self, number: int) -> int:
        if number in self.nToI and self.nToI[number]:
            return self.nToI[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)