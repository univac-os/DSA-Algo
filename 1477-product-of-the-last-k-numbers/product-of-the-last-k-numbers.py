class ProductOfNumbers:
    """
    arr and for product we can have prefixSum type  arr[idx]=(val,prefix) but we want no product after addition so arr will have only prefix product only
    """
    def __init__(self):
        self.arr=[1] #added a dummy start

    def add(self, num: int) -> None:
        if num==0:
            #reset the product
            self.arr=[1]
        else:
            self.arr.append(self.arr[-1]*num)
            
    def getProduct(self, k: int) -> int:
        if k>=len(self.arr):
            return 0
        return (self.arr[-1]//self.arr[-(k+1)])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)