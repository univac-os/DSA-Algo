class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #looks like merge interval ,we have start time and time taken by it
        t=0
        total=0
        for arr,time_taken in customers:
            if t>arr:
                #merging
                total+=t-arr
            else:
                t=arr #new interval
            total+=time_taken
            t+=time_taken
        return total/len(customers)