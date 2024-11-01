class Solution:
    def maximumSwap(self, num: int) -> int:
        # just like prefix sum we need to find max value from end and have the ptr 
        #to swap the ptr with current idx, O(n) and space O(n)
        # we need swap index and max_value idx so we here check if value > max_val
        num=list(str(num))
        max_idx=-1
        max_val='0'
        x=y=-1 #swap idx
        for idx,n in reversed(list(enumerate(num))):
            #find max
            if n>max_val:
                max_val=n
                max_idx=idx
            #find swap indexes
            if n< max_val:
                #we got swap index
                x,y=idx,max_idx
        num[x],num[y]=num[y],num[x]

        return int(''.join(num))
